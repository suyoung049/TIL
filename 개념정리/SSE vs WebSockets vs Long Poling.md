## SSE vs WebSockets vs Long Poling

### Server Sent Events

- it's possible for a server to send new data to a web page at any time, by pushing messages to the web page

- SSE (Client)

```javascript
//Client side implementation
//subscribe for messages
var source = new EventSource('URL');

//handle messages
source.onmessage = function(event) {
    //Do something with the data
    event.data;
};

//Handle build-in events
source.onopen
source.onmessage
source.onclose

//Handle custom events
source.addEventListenet("customEvent", handler);
```

- SSE (server: Node.js)

```java
//server implementation
function handler(response)
{
    response.writeHead(200, {
        'Content-Type : 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'    
    });
    
    response.write('id:UniqueID\n');
    response.write("data:" + data + '\n\n');
      
}

//SERVER
response.write('id: UniqueID\n');
response.write('event: add\n');
response.write('retry:10000\n');
response.write('data:' + data + '\n\n');

//CLIENT
source.addEventListener('add', function(event) {
    //do stuff with data
    event.data;
});
```



| Server Sent Event            | WebSockets                           |
| ---------------------------- | ------------------------------------ |
| Unidirectional               | Bidirectional                        |
| 6 Connections per browser    | No limit                             |
| Easier                       | More Complex                         |
| Limited                      | Extensible                           |
| UTF-8 text only              | Can send binary data                 |
| Great for Push Notifications | Great for realtime chat applications |

#### SSE Use cases

- Live Feed
- Showing client progerss
- Logging



#### SSE Pros and Cons

##### Pros

- Lightweight
- HTTP & HTTP/2 compatible
- Fierwall friendly (standard)

##### Cons

- Proxying is tricky
- L7 L/B challenging(timeouts)
- Stateful, difficult to horizontally scale



## 웹소켓 VS SSE



### 웹 소켓, SSE 장단점



- 웹 소켓 장점(확장성과 효율성)

  - 확장성을 고려할 때 웹 소켓이 Server-Sent Events (SSE)보다 효율적인 경우가 많습니다. 웹 소켓은 클라이언트와 서버 간의 양방향 통신을 제공하며, 실시간 데이터 전송에 적합한 프로토콜입니다. 다음은 웹 소켓의 확장성과 효율성을 강조하는 몇 가지 이유입니다:

    1. 단일 연결: 웹 소켓은 클라이언트와 서버 간에 단일 연결을 유지합니다. 이는 SSE와 달리 매 요청마다 새로운 연결을 만들 필요가 없다는 것을 의미합니다. 연결을 유지하는 것은 네트워크 부하를 줄이고, 서버 리소스를 효율적으로 관리하는 데 도움이 됩니다.
    2. 양방향 통신: 웹 소켓은 클라이언트와 서버 간에 양방향 통신을 지원합니다. 클라이언트가 서버로부터 실시간 업데이트를 받을 수 있을뿐만 아니라, 클라이언트도 서버로 데이터를 보낼 수 있습니다. 이는 실시간 채팅, 협업 애플리케이션 등과 같이 실시간 상호작용이 필요한 경우에 특히 유용합니다.
    3. 효율적인 데이터 전송: 웹 소켓은 데이터 프레임을 효율적으로 압축하고 전송합니다. 이는 SSE보다 작은 데이터 패킷 크기를 가지며, 대역폭을 절약하고 네트워크 지연을 줄이는 데 도움이 됩니다.
    4. 이벤트 기반 아키텍처: 웹 소켓은 이벤트 기반 아키텍처를 쉽게 구현할 수 있습니다. 이벤트 기반 아키텍처는 비동기적으로 작업을 처리하고 확장성을 높일 수 있는 방식으로 동작합니다.

    그러나 SSE도 특정 상황에서 유용할 수 있습니다. SSE는 단방향 통신이며, 데이터 전송이 상대적으로 덜 빈번한 경우에 사용될 수 있습니다. 또한 SSE는 웹 브라우저에서 내장된 기능을 사용하여 구현할 수 있으며, 서버 측에서 추가적인 프로토콜 지원이 필요하지 않습니다.

    따라서, 확장성을 고려한다면 웹 소켓을 사용하는 것이 일반적으로 더 효율적일 수 있습니다. 웹 소켓은 실시간 양방향 통신을 제공하고, 효율적인 데이터 전송 및 이벤트 기반 아키텍처를 지원하여 확장성과 성능 면에서 우수한 선택입니다. 그러나 SSE는 단방향 통신에 적합하고, 웹 브라우저에서 내장된 기능을 사용하여 구현하기 쉽습니다. 따라서 상황과 요구 사항에 맞게 웹 소켓 또는 SSE를 선택해야 합니다.

- SSE 장점(단순한구현, 호환성, 리소스 자원 사용 덜함)

  - 단순한 구현: SSE는 기본적인 HTTP 기반 기술이며, 웹 브라우저에서 내장된 기능을 사용하여 구현할 수 있습니다. 이는 서버 측에서 추가적인 프로토콜 지원이 필요하지 않는다는 의미입니다. 웹 브라우저에서는 SSE를 쉽게 사용할 수 있으며, 클라이언트 측에서도 구현이 간단합니다 이는 웹 소켓과 달리 추가적인 비용이 적게 들고 리소스 자원 사용 덜하다는 장점으로 이어집니다.
  - 오류 처리: SSE는 연결이 유실되거나 중단된 경우 자동으로 재연결될 수 있는 기능을 제공합니다. 이는 네트워크 연결의 불안정성이 있는 경우에 유용합니다. SSE는 중간에 연결이 끊어진 경우 클라이언트가 서버에 재연결을 요청하고, 이어지는 이벤트 스트림을 다시 받을 수 있습니다.
  - 단방향 통신: SSE는 서버에서 클라이언트로의 단방향 통신을 지원합니다. 서버는 실시간 업데이트를 클라이언트로 보낼 수 있지만, 클라이언트는 서버로 데이터를 보낼 수는 없습니다. 이는 특정 시나리오에서 단방향 통신만 필요한 경우에 유용합니다.
  - 호환성: SSE는 일부 오래된 웹 브라우저에서도 지원됩니다. 웹 브라우저에서 SSE를 지원하지 않는 경우에는 폴링 기법을 사용하여 구현할 수 있습니다. 이는 SSE를 이용하여 구현한 애플리케이션을 오래된 브라우저와 호환시키기 쉽게 만들어 줍니다.
  - 리소스 자원 사용 감소: 

  따라서, 단순한 구현, 오류 처리, 단방향 통신 및 호환성 측면에서 SSE는 일부 상황에서 유용할 수 있습니다. 그러나 SSE는 웹 소켓과 비교할 때 양방향 통신, 효율적인 데이터 전송 및 이벤트 기반 아키텍처 등에서 제한이 있을 수 있습니다.

  

### 웹소켓의 서버 리소스 자원 에관한 애기



웹 소켓이 SSE보다 더 많은 서버 데이터를 사용하는 이유는 다음과 같은 요인에 기인합니다:

1. 양방향 통신: 웹 소켓은 클라이언트와 서버 간에 양방향 통신을 지원합니다. 따라서 클라이언트가 서버로 데이터를 보낼 수 있고, 서버는 클라이언트에게 데이터를 전송할 수 있습니다. 이에 따라 웹 소켓은 SSE보다 더 많은 데이터를 전송해야 할 수 있습니다.
2. 추가적인 프로토콜 오버헤드: 웹 소켓은 헤더와 프레임 등의 추가적인 프로토콜 오버헤드를 갖습니다. 이는 각각의 데이터 패킷에 포함되어 전송되는 정보로, SSE보다는 더 많은 데이터 용량을 차지하게 됩니다.
3. 연결 유지: 웹 소켓은 클라이언트와 지속적인 연결을 유지합니다. 연결 상태를 유지하려면 클라이언트와 서버 간의 핑-퐁(ping-pong) 메시지 교환 및 상태 관리를 해야 합니다. 이로 인해 웹 소켓은 SSE보다 더 많은 서버 리소스를 사용하게 됩니다.
4. 데이터 압축: 웹 소켓은 데이터 압축을 지원하는 경우가 많습니다. 압축된 데이터를 전송하려면 서버에서 데이터를 압축하고 클라이언트에서 압축을 해제해야 합니다. 이로 인해 웹 소켓은 데이터 압축을 위한 추가적인 처리를 수행하므로 SSE보다 더 많은 서버 데이터를 사용할 수 있습니다.

요약하자면, 웹 소켓은 양방향 통신, 추가적인 프로토콜 오버헤드, 연결 유지, 데이터 압축 등의 특성으로 인해 SSE보다 더 많은 서버 데이터를 사용할 수 있습니다. 이는 웹 소켓이 더 많은 유연성과 기능을 제공하는 대신 일부 더 많은 서버 리소스를 요구한다는 것을 의미합니다.

 

### 포스터 질문 내용

1. redis 사용할 때 LFU 정책으로 관리한다고 되어 있는데 어떻게 구현했는지
2. SSE 방식은 어떻게 구현했으며, Poling 대비 어느정도의 효과가 있는지
3. FCM 토큰 스케쥴링은 어떻게 구현했는지
4. WebRTC 온라인 여부와 DB의 관계(어떻게 구현했는지)



AI 미션 응답 속도 개선:
예시를 통해 살펴보겠습니다. 서버에서 API 요청을 받으면, redis에서 캐싱된 데이터가 충분한지 확인한 후에, 충분하지 않다면 AI에 요청합니다.
만약 캐싱된 데이터가 충분하다면 캐싱된 데이터를 랜덤하게 뽑아 사용자에게 응답합니다.
