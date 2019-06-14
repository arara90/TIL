1. **FORM** 

   1) action : submit 누르는 순간 input에 넣은 값이 (name속성에 지정) 박스에 담겨 도착하는 지점! 

   2) method : 방식 지정 (get, post)

    * **GET**? HTML을 줘! 

      ```html
      <form action="/catch/" method="GET">
          던질거 : <input type="text" name="message">
          <input type="submit" value="submit">
      </form>
      ```

       *  http://127.0.0.1:8000/catch/?message=hello 

         http://127.0.0.1:8000/**action**/?**name**=value
      
   * **POST?**

     1) Forbidden(403) error! 

     * CSRF 토큰을 통한 검증이 필요하다!

       ```html
       <body>
           <form action="/user_create/" method="POST">
               {% csrf_token %}
               이름: <input type="text" name="name">
               패스워드: <input type="text" name="pwd">
               <input type="submit" value = "submit">
           </form>
       </body>
       ```

     * 개발자 모드에서 확인해보면?

       ![개발자모드](.\imgs\3_form\img.PNG)

       