# baekjoon_python

백준 알고리즘 최소 하루 3개 풀이

언어: 파이썬



에라토스테네스의 체
위키백과: https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
위키백과, 우리 모두의 백과사전.
둘러보기로 가기검색하러 가기
에라토스테네스의 체
수학에서 에라토스테네스의 체는 소수(素數, 발음: [소쑤])를 찾는 방법이다. 고대 그리스 수학자 에라토스테네스가 발견하였다.


목차
1	알고리즘
1.1	에라토스테네스의 체를 프로그래밍 언어로 구현
2	같이 보기
3	각주
알고리즘
2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다. 그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
자기 자신을 제외한 2의 배수를 모두 지운다.
남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
자기 자신을 제외한 3의 배수를 모두 지운다.
남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
자기 자신을 제외한 5의 배수를 모두 지운다.
남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
자기 자신을 제외한 7의 배수를 모두 지운다.
위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
그림의 경우, {\displaystyle 11^{2}>120}{\displaystyle 11^{2}>120}이므로 11보다 작은 수의 배수들만 지워도 충분하다. 즉, 120보다 작거나 같은 수 가운데 2, 3, 5, 7의 배수를 지우고 남는 수는 모두 소수이다.

에라토스테네스의 체를 프로그래밍 언어로 구현
◆ C++로 이 알고리즘을 다음과 같이 구현할 수 있다.

void Eratos(int n)
{
    /*  만일 n이 1보다 작거나 같으면 함수 종료 */
    if (n <= 1) return;

    /*	2부터 n까지 n-1개를 저장할 수 있는 배열 할당
		배열 참조 번호와 소수와 일치하도록 배열의 크기는
		n+1 길이만큼 할당(인덱스 번호 0과 1은 사용하지 않음)	*/
	bool* PrimeArray = new bool[n + 1];

	/*  배열초기화: 처음엔 모두 소수로 보고 true값을 줌	*/
	for (int i = 2; i <= n; i++)
	    PrimeArray[i] = true;

	/*	에라토스테네스의 체에 맞게 소수를 구함
		만일, PrimeArray[i]가 true이면 i 이후의 i 배수는 약수로 i를
		가지고 있는 것이 되므로 i 이후의 i 배수에 대해 false값을 준다.
		PrimeArray[i]가 false이면 i는 이미 소수가 아니므로 i의 배수 역시
		소수가 아니게 된다. 그러므로 검사할 필요도 없다.
또한 i*k (k < i) 까지는 이미 검사되었으므로 j시작 값은 i*2 에서 i*i로 개선할 수 있다.
	*/
	for (int i = 2; i * i <= n; i++)
	{
		if (PrimeArray[i])
			for (int j = i * i; j <= n; j += i)
			    PrimeArray[j] = false;
	}

	// 이후의 작업 ...
}
◆ java 로 구현

public class Eratos {
	public static void main(String[] args) {
		// ArrayList로 구현
		ArrayList<Boolean> primeList;

		// 사용자로부터의 콘솔 입력
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();

		// n <= 1 일 때 종료
		if(n <= 1) return;

		// n+1만큼 할당
		primeList = new ArrayList<Boolean>(n+1);
		// 0번째와 1번째를 소수 아님으로 처리
		primeList.add(false);
		primeList.add(false);
		// 2~ n 까지 소수로 설정
		for(int i=2; i<=n; i++ )
			primeList.add(i, true);

		// 2 부터  ~ i*i <= n
		// 각각의 배수들을 지워간다.
		for(int i=2; (i*i)<=n; i++){
			if(primeList.get(i)){
				for(int j = i*i; j<=n; j+=i) primeList.set(j, false);
				//i*i 미만은 이미 처리되었으므로 j의 시작값은 i*i로 최적화할 수 있다.
			}
		}
		StringBuffer sb = new StringBuffer();
		sb.append("{");
		for(int i=0; i<=n; i++){
			if(primeList.get(i) == true){
				sb.append(i);
				sb.append(",");
			}
		}
		sb.setCharAt(sb.length()-1, '}');

		System.out.println(sb.toString());

	}
}

◆ python(3.6.4)으로 구현[1]

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
결과:

prime_list(20)
[2, 3, 5, 7, 11, 13, 17, 19]

max(prime_list(1000000))
999983
◆ Haskell 로 구현

타입 정보 있는 버전 (권장)

primes :: [Int]
primes = sieve [2..]
           where sieve :: [Int] -> [Int]
                 sieve (prime : xs) = prime : sieve [x | x <- xs, x `mod` prime /= 0]
타입 정보 없는 버전 (Haskell의 타입 추론 이용)

primes = sieve [2..]
           where sieve (prime : xs) = prime : sieve [x | x <- xs, x `mod` prime /= 0]
결과:

-- 처음 소수 10개 찾기
take 10 primes
[2,3,5,7,11,13,17,19,23,29]

-- 100보다 큰 소수 5개 찾기
take 5 $ filter (>100) primes
[101,103,107,109,113]
