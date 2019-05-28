## Static Web

* 단순하게 무수히 많은 파일이 존재하는 서버에 요청을 보내 원하는 파일을 불러온다

* 파일들을 주고 받는 웹

* 주소는 파일명으로 끝난다

## Dynamic Web

* 연산결과, 처리결과를 보여준다

* URL(Uniform Resource Locator): 네트워크상에서 자원이 어디 있는지 알려주기 위한 고유 규약/ URL은 웹사이트 주소 뿐만 아니라 컴퓨터 네트워크상의 자원을 모두 나타낼 수 있다

____________



# Static Web 작성하기

## HTML(Hyper Text Markup Language)

* 텍스트의 순서 없이 이어주는 포인트(link)들을 통해 자유롭게 이동 가능하고(Hyper Text/ hyper text transfer protocol), 의미 파악이 용이하도록 정렬된(Markup/ tag들을 사용 ex. <h1>, <p>..) 언어(Language)

* Hyper Text를 Markup하기 위한 언어

* tab --> 자동완성

* ```
  <!DOCTYPE html> # 사용하는 문서 종류 선언
  <html>
      <head> # 문서제목등 문서 관련 정보/ 브라우저에 나타나지 않음
      <body> # 브라우저 화면에 나타나는 정보로 실제 내용에 해당
      
      </body>
      </head>
  </html>
  ```

* 주석 -->  <!-- Comment -->

* Tag

  요소(element): 태그 + 내용(contents)

  속성: <a href(속성명)="https://google.com"(속성값)/>

  =사이는 띄어쓰지 않는 것이 권장된다

  id, class, style 속성은 태그와 상관없이 모두 사용 가능하다

* Dom Tree: 태그는 중첩되어 사용가능하며 관계성을 가진다
* 시맨틱 태그: 컨텐츠의 의미를 성명하는 태그
  - header, nav, article, aside, section(article의 부모태그), footer...

https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjZ9LWdib3iAhVGxYsBHWuSD6IQjRx6BAgBEAU&url=https%3A%2F%2Fwww.w3schools.com%2Fhtml%2Fhtml5_semantic_elements.asp&psig=AOvVaw32BAf4xdQlTtXd788A3iB3&ust=1559093283145519

* ! + tab --> 자동완성
* poiemaweb.com 참고



## CSS

* 스타일시트 언어

* head 태그 안에, style 태그에 작성

* ```
  <head>
          <title> Hello word </title>
          <style>
              /* CSS 주석 */
  
              /* 1. tag name */
              /*선택자(header) 태그의 색(속성)을 빨강(값)으로*/
              header {
                  color: red;
                  font-size: 20px;
              }
  
              /* 2. select all */
              /* *--> 전체 적용 */
              * {
                  margin: 0;  // element 밖의 여백
                  padding: 0; // 자신의 여백
              }
  
              /* 3. id selector */
              #foot {
                  background-color: black;
                  color: white;
              }
  
              /* 4. class selector */
              .art {
                  font-size: 30px;
                  color: green;
              }
  
              /* 5. parent child */
              /* ol의 자식 태그인 li 태그에 적용 */
              ol > li {
                  color: yellow;
              }
              p > i > b {   /* p b: 모든 p 태그 안의 모든 b 태그 */
                  color: gray;
                  color: gray;
              }
  
          </style>
          <link rel="stylesheet" href="index.css"> <!-- css 파일을 만들어 style 적용 -->
      </head>
  ```

* ```
  /* CSS 주석 */
  // 한줄 주석
  ```

* ```
  인라인
  <nav style="color: blue;">nav</nav>
  ```

* ```
  가장 많이 사용된다
  <link rel="stylesheet" href="index.css"> <!-- css 파일을 만들어 style 적용 -->
  ```