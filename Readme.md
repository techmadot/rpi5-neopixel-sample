# Raspberry Pi 5で動作するNeoPixelサンプル

タイトルの通りですが、 Raspberry Pi 5でもNeoPixelが動いたので、サンプルコードを登録しました。手元の WS2012Bを使っているLEDテープやLEDパネルなどで動作を確認できました。

このサンプルは https://github.com/rpi-ws281x/rpi-ws281x-python に含まれていた strandtest.py を移植したものです。


## 動作環境

Raspberry Pi 5
- 64bit Raspberry Pi OS Lite
    - 2024/7/04版
- WS2012B デバイス
- Python 3.11.2

## ビルドと実行

### 環境構築


仮想環境を用意して、必要なモジュールをインストールします。

```
$ sudo apt install python3-pip  ## pipがシステムにインストールされていないならインストールすること
$ python3 -m venv .venv
$ source .venv/bin/activate  ## 仮想環境を有効化
$ pip3 install adafruit-circuitpython-neopixel-spi
```

#### 動作確認したときの各種パッケージのバージョン情報

```bash
$ pip list
Package                                  Version
---------------------------------------- -------
Adafruit-Blinka                          8.45.2
adafruit-circuitpython-busdevice         5.2.9
adafruit-circuitpython-connectionmanager 3.1.1
adafruit-circuitpython-neopixel-spi      1.0.9
adafruit-circuitpython-pixelbuf          2.0.4
adafruit-circuitpython-requests          4.1.3
adafruit-circuitpython-typing            1.10.3
Adafruit-PlatformDetect                  3.71.0
Adafruit-PureIO                          1.1.11
binho-host-adapter                       0.1.6
numpy                                    2.0.0
pip                                      23.0.1
pyftdi                                   0.55.4
pyserial                                 3.5
pyusb                                    1.2.1
RPi.GPIO                                 0.7.1
rpi-ws281x                               5.0.0
setuptools                               66.1.1
sysv-ipc                                 1.1.0
typing_extensions                        4.12.2
```


### デバイスとの配線について

Raspberry Pi 5のピンヘッダからデバイスに対して接続します。
3.3VやGNDの配線が必要なほか、SPIのMOSIのピンを使用します。
MOSIのピンは物理ピン番号で"19"です。GPIOピンの番号で"10"となっています。

|物理ピン    | 1   | 6   | 19 |
|-----------|-----|-----|----|
|NeoPixel   | Vcc | GND | DI |


### 実行

仮想環境の中から、本リポジトリのコードを実行するとNeoPixel(フルカラーLED)が点灯してアニメーションします。
Ctrl+Cの押下で、LEDを消灯してプログラムを停止します。

https://github.com/techmadot/rpi5-neopixel-sample/assets/101812623/413400fd-4dc7-4aa7-9f12-72d352871415

## 備考

Raspberry Pi 5では動作しないという rpi_ws281x の話を見かけて心配しておりました。しかしSPIの信号線を使うことでうまく点灯制御できているようです。


### 免責事項

動作保証があるわけではないので、利用する際には各自の責任でお願いします。

