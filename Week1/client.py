from socket import *

print("소켓을 이용한 채팅 프로그램입니다.")

# 접속 정보 설정
host = "127.0.0.1"
port = 8080

#클라이언트 소켓 설정
client_socket = socket(AF_INET, SOCK_STREAM)
# 서버 연결
client_socket.connect((host, port))
print("연결이 확인 되었습니다.")

while True:
    # 데이터를 입력받아 서버에 전달
    send_data = input("나: ")
    client_socket.send(send_data.encode("utf-8"))
    # 종료 조건 설정
    if send_data == "종료":
        print("연결이 종료 되었습니다.")
        break
    
    # 서버로부터 데이터를 전달받음 (최대 1024 바이트)
    recv_data = client_socket.recv(1024)
    print("상대방:", recv_data.decode("utf-8"))
    # 종료 조건 설정
    if recv_data.decode("utf-8") == "종료":
        print("연결이 종료 되었습니다.")
        break