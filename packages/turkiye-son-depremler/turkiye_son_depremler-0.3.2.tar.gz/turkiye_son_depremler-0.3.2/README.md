## TÜRKİYE VE YAKIN ÇEVRESİNDEKİ SON 500 DEPREM

#### BOĞAZİÇİ ÜNİVERSİTESİ KANDİLLİ RASATHANESİ VE DEPREM ARAŞTIRMA ENSTİTÜSÜ (KRDAE) BÖLGESEL DEPREM-TSUNAMİ İZLEME VE DEĞERLENDİRME MERKEZİ (BDTİM)

## Kurulum

```bash
pip install turkiye-son-depremler
```
## Kullanım

```bash
from turkiye_son_depremler import DepremData

depremler = DepremData().data

for deprem in depremler:
    print(deprem['TarihSaat'], deprem['Konum'], deprem['Siddet'])

```