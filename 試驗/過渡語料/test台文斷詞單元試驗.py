# -*- coding: utf-8 -*-
import io
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase


from 臺灣言語服務.過渡語料 import 過渡語料處理


class test台文斷詞單元試驗(TestCase):
    公家內容 = {'種類':  '語句', '年代':  '2018', }

    @patch('臺灣言語服務.過渡語料.過渡語料處理.台文語料斷詞')
    def test_指令的參數愛運作正常(self, 台文語料斷詞mock):
        with io.StringIO() as err:
            call_command(
                '台文用語料斷詞',
                '--參考', 'su-tian', '--參考', 'su-lui',
                '--欲斷詞', 'ti-a',
                stderr=err
            )
        台文語料斷詞mock.assert_called_once_with(
            ['su-tian', 'su-lui'],
            ['ti-a']
        )

    @patch('臺灣言語服務.過渡語料.過渡語料處理.台文語料斷詞')
    def test_指令顯示數量(self, 台文語料斷詞mock):
        台文語料斷詞mock.return_value = 333
        with io.StringIO() as err:
            call_command(
                '台文用語料斷詞',
                '--參考', 'su-tian', '--參考', 'su-lui',
                '--欲斷詞', 'ti-a',
                stderr=err
            )
        self.assertIn('斷詞 333 句', err.getvalue())

    @patch('sys.exit')
    @patch('臺灣言語服務.過渡語料.過渡語料處理.台文語料斷詞')
    def test_無語料愛錯誤(self, 台文語料斷詞mock, exitMock):
        台文語料斷詞mock.side_effect = ValueError()
        with io.StringIO() as err:
            call_command(
                '台文用語料斷詞',
                '--參考', 'su-tian', '--參考', 'su-lui',
                '--欲斷詞', 'ti-a',
                stderr=err,
            )
            call_command('台文語料斷詞', stderr=err)
        exitMock.assert_called_once_with(1)

    def test_有斷著詞(self):
        過渡語料處理.objects.create(
            來源='su-tian', 文本='我｜gua2 愛｜ai3 豬-仔｜ti1-a2', **self.公家內容
        )
        過渡語料處理.objects.create(
            來源='ti-a', 文本='豬仔愛我', **self.公家內容
        )
        過渡語料處理.台文語料斷詞(['su-tian'], ['ti-a'])
        過渡語料處理.objects.get(文本='豬-仔｜ti1-a2 愛｜ai3 我｜gua2')

    def test_回傳處理數量(self):
        過渡語料處理.objects.create(
            來源='su-tian', 文本='我｜gua2 愛｜ai3 豬-仔｜ti1-a2', **self.公家內容
        )
        過渡語料處理.objects.create(
            來源='ti-a', 文本='豬仔愛我', **self.公家內容
        )
        斷詞數量 = 過渡語料處理.台文語料斷詞(['su-tian'], ['ti-a'])
        self.assertEqual(斷詞數量, 1)

    def test_來源無出現(self):
        過渡語料處理.objects.create(
            來源='ti-a', 文本='豬仔愛我', **self.公家內容
        )
        with self.assertRaises(ValueError):
            過渡語料處理.台文語料斷詞(['su-tian'], ['ti-a'])

    def test_目標無出現(self):
        過渡語料處理.objects.create(
            來源='su-tian', 文本='我｜gua2 愛｜ai3 豬-仔｜ti1-a2', **self.公家內容
        )
        with self.assertRaises(ValueError):
            過渡語料處理.台文語料斷詞(['su-tian'], ['ti-a'])
