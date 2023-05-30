include "k1-smtp.h"

int mail_action(int __soc, char *__fromMail);
int rcpt_action(int __soc, char *__toMail);
int data_action(int __soc, char *__fromMail, char *__toMail);

//*******************************************************
// SMTP処理 smtp_process
//  [ARGUMENT]
//    __soc : ソケットディスクリプタ
//  [RETURN]
//    Success : 0
//    Error   : -1
//*******************************************************
int smtp_process(int __soc){
  char sendBuf[BUFSIZE], recvBuf[BUFSIZE];
  char fromMail[BUFSIZE]; //配信メールアドレス
  char toMail[BUFSIZE];   //宛先メールアドレス
  int sendLen, recvLen;
  int flag;

  //サーバからのリプライコード受信
  recvLen = recv(__soc, recvBuf, BUFSIZE, 0);
  recvBuf[recvLen] = '\0';
  printf("<===  %s", recvBuf);

  //HELOコマンド
  sendLen = sprintf(sendBuf, "%s localhost%s", HELO, ENTER);
  printf("===> %s", sendBuf);
  send(__soc, sendBuf, sendLen, 0);

  recvLen = recv(__soc, recvBuf, BUFSIZE, 0);
  recvBuf[recvLen] = '\0';
  printf("<=== %s", recvBuf);

  //MAILコマンド・アクション
  if( (flag = mail_action(__soc, fromMail)) < 0 ) return flag;

  //RCPTコマンド・アクション
  if( (flag = rcpt_action(__soc, toMail)) < 0 ) return flag;

  
  //メール本文・アクション
  if( (flag = data_action(__soc, fromMail,toMail)) < 0 ) return flag;


}//END smtp_process()

//**************************************************************
// MAILコマンド・アクション mail_action
//  [ARGUMENT]
//    __soc      : ソケットディスクリプタ
//    __fromMail : 配信メールアドレス格納用バッファのポインタ
//  [RETURN]
//    Success : 0
//    Error   : -1
//**************************************************************
int mail_action(int __soc, char *__fromMail){
  char sendBuf[BUFSIZE], recvBuf[BUFSIZE];
  char tmp[BUFSIZE];
  int resCode;
  int sendLen, recvLen;
  int fromLen;

  printf("\n*配信メールアドレス(From)を入力:");
  fgets(__fromMail, BUFSIZE, stdin);
  fromLen = strlen(__fromMail);
  __fromMail[fromLen-1] = '\0';
  fromLen--;

  if(fromLen < 1) return -1;

  sendLen = sprintf(sendBuf, "%s FROM:%s%s", MAIL, __fromMail, ENTER);
  printf("===> %s", sendBuf);
  send(__soc, sendBuf, sendLen, 0);
  recvLen = recv(__soc, recvBuf, BUFSIZE, 0);
  recvBuf[recvLen] = '\0';
  printf("<=== %s", recvBuf);
  
  sscanf(recvBuf,"%d %s", &resCode, sendBuf);

  if(resCode == SUCCESS_CODE) return 0;
  else return -1;  


}//END mail_action()


//**************************************************************
// RCPTコマンド・アクション rcpt_action
//  [ARGUMENT]
//    __soc      : ソケットディスクリプタ
//    __toMail : 宛先メールアドレス格納用バッファのポインタ
//  [RETURN]
//    Success : 0
//    Error   : -1
//**************************************************************
int rcpt_action(int __soc, char *__toMail){
  char sendBuf[BUFSIZE], recvBuf[BUFSIZE];
  char tmp[BUFSIZE];
  int resCode;
  int sendLen, recvLen;
  int toLen;
  
  printf("\n*宛先メールアドレス(to)を入力:");
  fgets(__toMail, BUFSIZE, stdin);
  toLen = strlen(__toMail);
  __toMail[toLen-1] = '\0';
  toLen--;

  if(toLen < 1){
    return -1;
  }

  sendLen = sprintf(sendBuf, "%s TO:%s%s", RCPT, __toMail, ENTER);
  printf("===> %s", sendBuf);
  send(__soc, sendBuf, sendLen, 0);
  recvLen = recv(__soc, recvBuf, BUFSIZE, 0);
  recvBuf[recvLen] = '\0';
  printf("<=== %s", recvBuf);
  
  sscanf(recvBuf,"%d %s", &resCode, recvBuf);

  if(resCode == SUCCESS_CODE){
    return 0;
  }
  else{
    return -1;
  }


}//END rcpt_action()


//**************************************************************
// メール本文・アクション data_action
//  [ARGUMENT]
//    __soc      : ソケットディスクリプタ
//    __froMail  : 配信メールアドレスのポインタ
//    __toMail   : 宛先メールアドレスのポインタ
//  [RETURN]
//    Success : 0
//    Error   : -1
//**************************************************************
int data_action(int __soc, char *__fromMail, char *__toMail){
  char    sendBuf[BUFSIZE],recvBuf[BUFSIZE];
  int     sendLen,recvLen,resCode;
  char    msgBuf[BUFSIZE];

  sendLen = sprintf(sendBuf,"%s%s",DATA,ENTER);
  send(__soc,sendBuf,sendLen,0);

  recvLen = recv(__soc,recvBuf,BUFSIZE,0);
  recvBuf[recvLen] = '\0';
  printf("%s\n",recvBuf);

  sendLen = sprintf(sendBuf,"FROM:%s%s",__fromMail,ENTER);
  send(__soc,sendBuf,sendLen,0);

  sendLen = sprintf(sendBuf,"TO:%s%s",__toMail,ENTER);
  send(__soc,sendBuf,sendLen,0);

  printf("Input Subject:");
  fgets(msgBuf,BUFSIZE,stdin);
  sendLen = sprintf(sendBuf,"Subject: %s%s",msgBuf,ENTER);
  send(__soc,sendBuf,sendLen,0);

  while(1){
    fgets(msgBuf,BUFSIZE,stdin);
    if(strncmp(msgBuf,".\n",2) == 0){
      sendLen = sprintf(sendBuf,"%s.%s",ENTER,ENTER);
      send(__soc,sendBuf,sendLen,0);
      break;
    }
    sendLen = strlen(msgBuf);
    send(__soc,msgBuf,sendLen,0);
  }

  recvLen = recv(__soc,recvBuf,BUFSIZE,0);
  recvBuf[recvLen] = '\0';
  printf("<===%s\n",recvBuf);

  sscanf(recvBuf,"%d %s",&resCode,msgBuf);
  if(resCode == SUCCESS_CODE){
    return 0;
  }
  else{
    return 1;
  }
}//END data_action()