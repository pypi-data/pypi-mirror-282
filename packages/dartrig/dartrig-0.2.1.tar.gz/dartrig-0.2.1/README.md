# Dart API/Web Data Rigger

### Dart API

API Reference: https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019001

#### corp_cls code
- Y : 유가
- K : 코스닥
- N : 코넥스
- E : 기타

#### rm code
- 유 : 본 공시사항은 한국거래소 유가증권시장본부 소관임
- 코 : 본 공시사항은 한국거래소 코스닥시장본부 소관임
- 채 : 본 문서는 한국거래소 채권상장법인 공시사항임
- 넥 : 본 문서는 한국거래소 코넥스시장 소관임
- 공 : 본 공시사항은 공정거래위원회 소관임
- 연 : 본 보고서는 연결부분을 포함한 것임
- 정 : 본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람
- 철 : 본 보고서는 철회(간주)되었으니 관련 철회신고서(철회간주안내)를 참고하시기 바람

## Usage

```python
from dartrig import DartAPI

keys = [
    "{YOUR_API_KEY_01}",
    "{YOUR_API_KEY_02}"
]

dart = DartAPI(keys=keys)

# Get disclosure list
dart.get_disclosure_list(end_de='20210331')
```