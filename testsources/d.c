int main(void) {
	int a;
	int b = 0;

	int c = a;
	
	a = b;
//	b = 0;

	int d = a + b;

	char arr[100];
	arr[a] = 1;
	arr[b] = 1;
	arr[c] = 1;
	arr[d] = 1;
}
