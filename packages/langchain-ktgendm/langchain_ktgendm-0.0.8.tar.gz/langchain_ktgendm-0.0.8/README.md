# KTGenDM Agent

KTGenDM Agent 프로젝트는 LangChain을 기반으로 생성형 대화를 처리하는 멀티턴 대화 에이전트입니다.

- [https://pypi.org/project/langchain-ktgendm/](https://pypi.org/project/langchain-ktgendm/)

## 설치 및 사용 방법

KTGenDM Agent를 설치하고 사용하는 방법은 다음과 같습니다.

### 요구 사항

- Python 3.8 이상
- 필요한 패키지들은 `requirements.txt` 파일에 명시되어 있습니다.

### langchain-ktgendm 패키지 사용 방법

예제 실행시 사용하는 HOST_URL은 `gendm`의 경우 개발용 호출을 위해 `http://localhost:10020`으로 사용합니다.
그외 POC서버의 HOST_URL은 관련 담당자께 문의 바랍니다.

- [/langchain_ktgendm/README.md](/langchain_ktgendm/README.md) : langchain_ktgendm 설치 및 사용방법 예시

### langchain-ktgendm 프로젝트 기여

clone 후에 ./langchain_ktgendm 소스 코드를 수정함으로서 기여할 수 있습니다.

[테스트]
```
$ git clone https://gitlab.dspace.kt.co.kr/GENDM/langchain-gendm
$ pip intall -r requirements.txt
$ sh test.sh
```

### langchain-ktgendm 패키지 배포

본 프로젝트의 [/langchain_ktgendm](/langchain_ktgendm) 경로는 배포용 디렉터리이며 개인 정보, 회사 정보 등을 포함하지 않으며 패키지 동작에 필요한 소스코드 정보만 포함합니다.
아래 배포 쉘을 이용해서 `langchain_ktgendm` 패키지 파일을 빌드하고 pypi에 배포할 수 있습니다.

```
$ sh build_whl.sh # 2번 build 도구를 통해 빌드 실행.
$ sh upload_pypi.sh # 배포시 pypi 키가 필요하며, 키 정보는 담당자께 문의 바랍니다.
```


## 문의

프로젝트에 관한 문의는 jeong.jinwook@kt.com로 연락해 주세요.