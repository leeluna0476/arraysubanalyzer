int	main(void) {
	int i, j;
	i = j; // i-> lvalue, j->casted. lvalue to rvalue
		   // 그러나 declrefexpr은 모두 lvalue
		   // rvalue가 Integer Literal이 아니라 ImplicitCast라면... 그 cast된 declrefexpr의 referenceddecl이 초기화되었나 확인해야 함.
		   // i=j 이전에 j=1 따위... 있어야 함.
	char arr[100];
	arr[i] = 1; // i가 초기화되었다고 판단할 것인가?
				// 지금 그러고 있다. ㅋㅋ
}
