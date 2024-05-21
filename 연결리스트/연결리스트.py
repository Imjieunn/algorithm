dat = [-1] * 10000
pre = [-1] * 10000
nxt = [-1] * 10000
unused = 1


# traverse 함수
def traverse():
    cur = nxt[0]
    while cur != -1:
        print(dat[cur])
        cur = nxt[cur]


# addr : 배열 상에서 각 원소의 주소
# 13이 2번지이고, 13 뒤에 20을 추가하고 싶으면 insert(2,20) 호출
# insert 함수
def insert(addr, num):
    # 1. 새로운 원소를 생성
    dat[unused] = num
    # 2. 새 원소의 pre값에 삽입할 위치의 주소를 대입
    pre[unused] = addr
    # 3. 새 원소의 nxt값에 삽일할 위치의 nxt값을 대입
    nxt[unused] = nxt[addr]
    # 4. 삽입할 위치의 nxt값과 삽입할 위치의 다음 원소의 pre값을 새 원소로 변경
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    # 5. unused 1 증가
    unused += 1


# erase 함수
def erase(addr):
    # 1. 이전 위치의 nxt를 삭제할 위치의 nxt로 변경
    nxt[pre[addr]] = nxt[addr]
    # 2. 다음 위치의 pre를 삭제할 위치의 pre로 변경
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]
