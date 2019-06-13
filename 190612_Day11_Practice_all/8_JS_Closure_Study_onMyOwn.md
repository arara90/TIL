## Closure

댓글 수정 만들기

<http://chanlee.github.io/2013/12/10/understand-javascript-closure/>

클로저 : 외부함수의 변수에 접근할 수 있는 내부함수. (=Scope Chain)

 * Scope Chain
   	*  자신의 블럭내에 정의된 변수 접근
   	* 외부 함수의 변수에 대한 접근
   	* 전역 변수에 대한 접근

- 내부 함수는 외부 함수의 변수뿐만 아니라 파라미터에도 접근 가능.

  단, 내부 함수는 **외부 함수의 arguments객체를 호출할 수 없다.**

  하지만, **외부 함수의 파라미터는 직접 호출 가능** 

  

