# pisca-pisca

## Informações gerais

Para estilos disponíveis, consulte `pisca.py`.

Para criar uma sequência, utilize o arquivo `luzes.py`.

## Setup

* Protoboard

Consideramos LEDs 3mm 2v 20mA, e resistores de 65Ω 1/4W. Sua configuração pode ser diferente.

![Setup do protoboard (você pode trocar os pinos GPIO, desde que respeite o layout](https://i.imgur.com/dwi7PJB.png)

* * Esquemático

<img src="https://i.imgur.com/7ekLtjy.png" alt="Esquemático" style="height: 200px;"/>

* Script

Defina os pinos GPIO do Raspberry para cada um dos LEDs no arquivo `luzes.py`.
P.S.: você pode alterar de `GPIO.BCM` para `GPIO.BOARD`, se preferir; mas isso tem que ser feito em ambos os arquivos.

## Executando

`python3 luzes.py`
