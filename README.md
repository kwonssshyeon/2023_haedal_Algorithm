# 2023_summer_Algorithm
해달해커톤 2탄 - 알고리즘 스터디
## 작업 방법
1. main 브렌치의 최신 커밋에서 자신의 브렌치를 만들고 체크아웃한다.
    - 브렌치명 형식 : `날짜_이름`, ex) `0718_dong`
2. 자기 폴더에 오늘 날짜에 해당하는 폴더를 만들고, 해당 폴더에 `README.md` 파일과 소스 코드 파일을 만든다.
3. `README.md` 파일에는 오늘 푼 문제 중 정리하고 싶은 문제를 정리하여 작성한다.
4. 소스 코드 파일에는 정리한 문제에 대한 소스 코드를 기입한다.
5. 자기 폴더의 `README.md` 파일(ex. `/김동환/REAMD.md`)에 해당 폴더에 대한 링크를 기입한다.
    - 링크의 형식은 `[7월 18일](./0718/)` 해당 형태로 작성할 수 있다.
6. 작업이 끝나면 커밋하고, main 브렌치에 Merge한다.
    - 이때, 따로 질문할 것이 없거나 크게 공유할 것이 없으면 그냥 바로 Merge한다.
    - 만약 코드 리뷰를 받고 싶거나 공유하고 싶은게 있다면 PR을 통해 리뷰를 받고 Merge한다.
7. Merge가 끝나면 해당 작업 브렌치는 삭제한다.

### Git 사용법
``` bash
# 1. main 브렌치의 최신 커밋에서 자신의 브렌치를 만들고 체크아웃한다.
## main 브렌치에 체크아웃
git switch main
## 깃헙 원격 저장소에서 main 브렌치의 최신 버전을 가져옴. (다른 사람이 main 브렌치에 새로운 커밋을 머지했을 수 있으니)
git pull origin main
## 0718_dong 브렌치를 만들면서 체크아웃
git switch -c 0718_dong

# 2. 3. 4. 5. 는 Git과 무관

# 6. 작업이 끝나면 커밋하고, main 브렌치에 Merge한다.
## 작업했던 모든 파일들(변경사항)을 새로운 커밋(버전)의 대상으로 만들어준다.
git add .
## 새로운 커밋(버전)을 만든다. (커밋한다.)
git commit -m "적절한 설명을 꼭 적어주세요."

## 그냥 Merge
### main 브렌치로 체크아웃한다.
git switch main
### 0718_dong 브렌치에서 작업했던 결과물(커밋)들을 현재 브렌치(main)에 머지한다.
git merge 0718_dong
### 작업했던 결과물(커밋)들을 깃허브에 반영(푸쉬)한다.
git push origin main

## PR
### 작업 중이던 브렌치를 깃허브에 반영(푸쉬)한다.
git push origin 0718_dong
### github의 레포지토리 페이지에서 Pull Requests 섹션에 들어간다.
### New Pull Requests 버튼을 누르고, Base를 main으로 Compare를 0718_dong 브렌치로 설정한다.
### 적절한 제목 및 본문을 추가하고 Create Pull Requests 버튼을 누른다.
### 이후 적절히 리뷰 등을 받고 해당 페이지에서 머지할 수 있다.

# 7. Merge가 끝나면 해당 작업 브렌치는 삭제한다.
git branch -D 0718_dong
```

### Markdown 문법
<https://velog.io/@gidskql6671/Markdown-%EB%AC%B8%EB%B2%95>  
해당 페이지 참조해주세용
