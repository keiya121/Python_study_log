/*************************************
 * 演習課題No.1
 * SMTPクライアント
 * k1-smtp_client_main.c
 *************************************/

#include "k1-smtp.h"

int smtp_connect(char *__ipaddr, u_short __port);
int smtp_close(int __soc);

extern int smtp_process(int __soc);

int main(int argc, char *argv[]){
  int soc;   //ソケットディスクリプタ
  int flag;  //SMTP処理結果フラグ

  if(argc != 2){
    printf("Usage:%s smtp_server_ipaddress\n", argv[0]);
    exit(1);
  }
  
  //SMTPサーバ接続要求
  soc = smtp_connect(argv[1], SMTP_PORT);
  if(soc < 0){
    exit(1);
  }
  
  //SMTP処理
  flag = smtp_process(soc);

  //SMTPサーバ接続切断
  smtp_close(soc);

  if(flag == 0){
    printf("SMTPは正常に完了しました\n");
  }else{
    printf("SMTPはエラーにより中断されました\n");
  }
  return 0;

}//END main()

//*********************************************************
// SMTPサーバ接続要求 smtp_connect
//  [ARGUMENT]
//    __ipaddr : IPアドレスの文字列バッファへのポインタ
//    __port   : ポート番号
//  [RETURN]
//    Success  : ソケットディスクリプタ
//    Error    : -1
//*********************************************************
int smtp_connect(char *__ipaddr, u_short __port){
  int s,con_flag;
  struct sockaddr_in server;
  //ソケット作成
  s = socket(AF_INET, SOCK_STREAM, 0);
  if(s < 0)
    {
      perror("socket");
      return(-1);
    }     

  //サーバへのコネクション要求
  memset(&server, 0, sizeof(server));
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = inet_addr(__ipaddr);
  server.sin_port = htons(__port);
  con_flag = connect(s,(struct sockaddr*)&server,sizeof(server));
  if(con_flag < 0){
    perror("connect");
    return(-1);
  }
  return(s);


}//END smtp_connect()

//**************************************************
// SMTPサーバ接続切断 smtp_close
//  [ARGUMENT]
//    __soc : ソケットディスクリプタ
//  [RETURN]
//    Success : 0
//**************************************************
int smtp_close(int __soc){
  char sendBuf[BUFSIZE],recvBuf[BUFSIZE];
  int  sendLen,recvLen;

  //QUITコマンド
  sendLen = sprintf(sendBuf,"%s%s",QUIT,ENTER);
  send(__soc,sendBuf,sendLen,0);
  
  recvLen = recv(__soc,recvBuf,BUFSIZE,0);
  recvBuf[recvLen] = '\0';
  printf("<===%s",recvBuf);


  //コネクション切断
  close(__soc);


  return 0;

}//END smtp_close()