from socket import *

# 통신 정보 설정
ip = ""
port = 8080

# 서버 소켓 설정
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((ip, port))

# 연결 요청을 기다림
server_socket.listen(1)
print("{}번 포트로 접속 대기중 ...".format(port))

# 접속 확인
connection_socket, addr = server_socket.accept()
print("{}에서 접속이 확인 되었습니다.".format(addr))

while True:
    # 클라이언트로부터 데이터를 전달받음 (최대 1024 바이트)
    recv_data = connection_socket.recv(1024)
    # 클라이언트 메시지 출력
    print("상대방:", recv_data.decode("utf-8"))
    # 종료 조건 설정
    if recv_data.decode("utf-8") == "종료":
        print("접속이 종료되었습니다.")
        break

    # 데이터를 입력받아 클라이언트에게 전달
    send_data = input("나: ")
    connection_socket.send(send_data.encode("utf-8"))
    # 종료 조건 설정
    if send_data == "종료":
        print("접속이 종료되었습니다.")
        break