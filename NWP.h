 * 演習課題No.1
 * SMTPクライアント（ヘッダファイル)
 * k1-smtp.h
 ***************************************/

#ifndef _INCLUDE_KADAI_
#define _INCLUDE_KADAI_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <unistd.h>

#define SMTP_PORT 25         //SMTPサーバのポート番号
#define BUFSIZE   512        //バッファサイズ
#define ENTER     "\r\n"     //メッセージ終端<CR><LF>

//プロトコルコマンド
#define HELO  "HELO"
#define MAIL  "MAIL"
#define RCPT  "RCPT"
#define DATA  "DATA"
#define QUIT  "QUIT"

//レスポンスコード
#define SUCCESS_CODE  250

#endif