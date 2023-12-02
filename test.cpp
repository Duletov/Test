#include <iostream>
int summ(int *start, int len){
	int temp = 0;
	for(int i=0; i<len;i++){
		temp += *(start+i);
	}
	return temp;
}


int main(){
	int *ss;
	int b[5] = {1, 2, 3, 4, 5};
	std::cout << summ(b, 5); 
	return 0;
}
