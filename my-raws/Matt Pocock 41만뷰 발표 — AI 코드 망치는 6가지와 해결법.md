# Matt Pocock 41만뷰 발표 — AI 코드 망치는 6가지와 해결법

코드는 더 이상 비싸지 않다. 요즘
AI 업계 분위기가 이거였거든요.
근데 한 사람이 무대에 올라와서 정
반대로 외쳤습니다. 코드는 싸지
않다. 오히려 나쁜 코드는 그 어느
때보다 비싸다.이 한마디로 일주일
만에 40만 명을 끌어 모았어요. 그
사람이 정리한 AI 시대 여섯 가지
함정과 여섯 가지 처방 18분짜리
발표를 핵심만 추려서 정리해
드립니다. 특히 클로드 코드 쓰시는
분들한테 와닿을 한 마디가 있어요.
발표자가 이런 말을 했거든요. AI는
자기가 만든 미로에서 자기가 길을
잃는다. 이게 무슨 말인지 영상
중반에 풀어 드릴게요. 먼저 한 가지
미리 알려 드릴게요.이 영상에는
중간중간 발표자 본인 영상이 1분에서
2분 정도씩 그대로 들어갑니다. 한국
자막도 같이 띄울테니까 부담없이
보세요. 꼭이라 분이 2026년 4월
AI 엔지니어 컨퍼런스에서 발표한
소프트웨어 펀더멘터스 메터모어 덴
에버 18분짜리 발표해요. 오늘은
그걸 제 관점에서 풀어 드리는
해설입니다. 근데이 사람이 누구냐?
타입스크립트 커뮤니티에서는 그냥
타입스크립트 그 사람으로 통합니다.
토탈 타입스크립트라는 강의로 유명해진
분이에요. 이전에는 버셀에서 디벨로퍼
애드보 했고 그 전에는 X스테이트
코어팀에서 일했고요. 근데 여기까진
그냥 잘 나가는 TS 강사고 진짜
흥미로운 건 최근 1년이에요.이
사람이 타입스크립트에서 AI
엔지니어링으로 방향을 완전히
틀었거든요. AI 히어로라는 학습
플랫폼 만들고 클로드 코드 포리얼
엔지니어스라는 강의를 운영 중이에요.
이번 발표는 그 강의 만들면서 정리한
결론이에요. 한마디로 이런 발표예요.
타입스크립트로 유명해진 사람이 AI
엔지니어링으로 피보하면서 근데 알고
보니 옛날 펀더멘탈이 더 중요하더라고
결론된 발표. 그래서 40일만이 몰린
거고요.이 발표의 출발점부터 봐야
해요. 요즘 AI 업계에 스펙스투
코드 운동이라는게 있어요.
들어보셨어요? 한마디로 스펙만 잘
쓰면 AI가 코드 다 짜 준다. 문제
생기면 스펙만 고치고 컴파일러 다시
돌려라. 코드는 안 봐도 된다. 이런
흐름이에요. 근데 포코이 직접 해
봤대요. 결과가 어땠을까요?
컴파일러를 돌릴 때마다 코드가 더
망가졌어요. 한 번 돌리면 좀 별로,
두 번 돌리면 더 별로. 계속
돌렸더니 결국 갑이지. 그냥 쓰레기.
왜 이렇게 되냐? 프리그메틱
프로그래머라는 옛날 책에 나오는
소프트웨어 엔트로피라는 개념
때문이에요. 부분만 고치고 전체
설계를 안 보면 시스템은 점점
무너진다. 근데 스펙스투 코드가
정확히 그걸 하고 있었던 거예요.
부분만 고치고 컴파일로 돌리고 부분만
고치고 컴파일로 돌리고 그래서 폭이
무대에서 결론을 이렇게 내렸어요.
코드는 싸지 않다. 오히려 나쁜
코드는 그 어느 때보다 비싸다.
왜냐면 좋은 코드 베이스에서 AI가
진짜 빛나거든요. 변경하기 어려운
코드는 AI한테 줘봐야 AI도 못
살려요. 결국 AI 시대일수록
펀더멘탈이 더 중요해진다는게이 발표의
핵심 명제입니다. 자, 이걸 무대에서
본인이 어떻게 던졌는지 본인 발표를
잠깐 보시죠. Raise your
hand if you've heard
that phrase before
that code is cheap.
Yeah.
Well, I don't think
this is right. I
think code is not
cheap. In fact, bad
code is the most
expensive it's ever
been. Because if you
have a codebase
that's hard to
change, you're not
able to take all of
the bounty that AI
can offer. AI in a
good codebase
actually does really
well.
And this means good
codebases matter
more than ever means
software
fundamentals matter
ever.
명제 위에 여섯 가지 함정과 여섯
가지 처방이 올라옵니다. 여섯 개 다
옛날 책 더하기 자기가 직접 만든
클로드 코드 스킬인데이 중 한 스킬은
기터브에서 별일만 3,000개를
받았어요. 지금부터 여섯 개 차례로
갑니다. 첫 번째 함정 AI가
머릿속에 있던 그 아이디어랑 완전히
다른 걸 만들어요. 본인이 머리에
그렸던 거랑 결과물이 어긋나는 거.
클로드 코드 좀 써 본 분들은
100% 겪어 봤을 거예요. 포콕의
진단은 이래요. 프레드릭 브룩스라는
거장이 디자인 컨셉이라는 개념을
얘기했거든요. 두 사람이 뭔가를 같이
만들 때 둘 사이에 떠다니는 보이지
않는 이걸 만들고 있다는 감각이
있대요. 마크다운에 적을 수가 없는
거. 근데 그게 사람이랑 AI
사이에서는 절대 공유가 안 되고
있다는 거죠. 처방이 그라는
스킬이에요. 신문해 줘라는 뜻이죠.
본체는 단 두 줄이에요.이 계획의
모든 측면을 끝까지 신문해라. 우리가
같은 이해에 도달할 때까지. 이거 한
줄 넣오면 AI가 사용자한테 40개,
60개, 많을 땐 100개 질문을
던져요.이 스킬이 기터부에서 별일만
3,000개를 받았어요. 그냥
바이럴됐어요. 포콕 본인은 클로드
코드 기본 플랜 모드보다 이게 낫다고
단언합니다. 플랜 모드는 너무 빨리
결과물부터 만들려고 한다고. 같은
이해에 도달하는게 먼저라는 거예요.
자, 본인이 무대에서이 스킬을 어떻게
풀어서 설명했는지 본인 입으로
들어볼게요. 두 번째 함정.
skill. The skill is
very very simple.
It's called Grill Me
and it looks like
this. Interview me
relentlessly about
every aspect of this
plan until we reach
a shared
understanding. Walk
down each branch of
the design tree,
which is another
thing from Frederic
P. Brooks, resolving
dependencies between
decisions one by
one. This skill is
like uh the repo
containing this
skill has like
13,000 stars or
something. Like it
just went nuts, went
viral. People love
this thing. it.
These couple of
lines means the AI
asks you like 40
questions, 60
questions. I've had
it ask people 100
questions before
it's satisfied.
They've reached a
shared understanding
and it means it
turns the AI into a
kind of adversary
where it's just
continually pinging
you ideas and trying
to reach a shared
understanding. And
that means that the
conversation that
you then generate,
you can take that
and turn it into a
product requirements
document or
something. or if
it's a small change,
you can just uh do
uh turn it directly
into issues
and then your AFK
agent will then pick
it up. And don't add
me on this, but I
personally believe
this is better than
the default plan
mode in the tool
that I use, which is
claw code. Plan mode
is extremely eager
to create an asset.
AI가 너무 장황해요. 같은 걸 자꾸
다른 단어로 풀어 말하는 거. 분명히
같은 뜻인데 매번 표현이 달라요.
이거 왜 이러는 줄 아세요? 포코의
비유가 진짜 좋아요. 옛날에 도메인
전문가랑 일해 본 적 있는 개발자라면
알 거예요. 마이크로칩 회사
클라이언트랑 일하는데 전문 용어가 안
맞으면 코드 자체가 어긋나잖아요.
그게 지금 AI랑 나 사이에서 똑같이
일어나고 있다는 거예요. 같은 언어로
말 안 하고 있는 거죠. 처방은
도메인 드리븐 디자인에 유비
Qu쿼터스 랭귀지라는 개념을 가져오는
거예요. 유비 쿼터스 언어 어디서나
통하는 언어 코드 베이스를 한번
스캔해서 거기서 쓰는 용어들을 다
추출해요. 그리고 마크다운 사전을
만들어요. 사람도 보고 AI도 보는
공통 단어집이죠. 이걸 항상 띄워놓고
AI랑 같이 쓴다는 거예요. 포코이
이거 도입하고 나서 AI가 생각하는
방식 자체가 덜 벌보스해졌다고 해요.
결국 사람이랑 같은 단어를 써야 같은
결과가 나오는 거죠. 세 번째 함정
AI가 의도대로 만들었는데 안
돌아가요. 코드는 그럴 듯하게 짰는데
실행하면 터져요. 이것도 익숙하시죠?
피드백 루프가 있긴 해요. 타입,
체커, 테스트, 브라우저 접근. 근데
LLM이이 도구들을 잘 못 써요. 한
번에 너무 많이 만들어 놓고 그제서야
어, 이거 타입 체크해야겠네. 늦게
깨달아요. 이미 망가진 다음에 보는
거예요. 여기서 포코이 인용한 비유가
진짜 인상적이에요. 프레그메틱
프로그래머에 나오는 아웃러닝
헤드라이트. 헤드라이트가 비추는
거리보다 빨리 달리면 사고 난다는
뜻이에요. 피드백의 속도가 곧 너의
속도 제한이다. 사람이 운전할 때도
마찬가지지만 AI한테 코딩시킬 때도
똑같다는 거예요. 그래서 처방이
뭐냐? TDD 테스트 주도
개발이에요. 옛날 방법인데 이게
LM한테 더 중요해요. 왜냐?
테스트를 먼저 쓰면 AI가 강제로
작은 단위로 움직이게 되거든요. 큰
거 한 번에 못 만들어요. 한 단계씩
가야 돼요. 헤드라이트 안 추월하게
되는 거죠. 근데 여기서 또 함정이
있어요. td 하려고 보니까 테스트
자체가 어려워요. 어떤 단위로
자를지, 뭘 모기할지, 어떤 동작을
검증할지 결정해야 할게 너무 많아요.
그래서 폭기 통차를 던져요. 좋은
코드 베이스는 테스트하기 쉬운 코드
베이스다. 결국 또 펀더멘탈 문제로
돌아온 거예요. 이걸 풀어주는 책이
존 오스터 하우이라는 분이 쓴
필로소피 오브 소프트웨어
디자인이에요. 거기 나오는 핵심 개념
두 개. 섀우 모듈, 대딥 모듈.
섀우 모듈은 작은 모듈, 잔뜩,
인터페이스도 복잡. 미로 같은
거예요. 어디 들어가야 할지 모르겠는
딥 모듈은 반대예요. 큰 기능을
단순한 인터페이스 뒤에 숨겨 놨어요.
입구는 간단한데 안쪽이 깊은 거.
근데 여기서 진짜 충격적인게 있어요.
AI가 자기가 만든 섀우 모듈을
미로해서 자기가 길을 잃어요. 그래서
처음 AI가 자기 미로에 갇힌다고
말씀드린 거예요. 이게 무슨 말이냐면
AI한테 그냥 코드자라고 하면 AI는
작은 모듈을 잔뜩 만들어요. 디폴트가
섀우예요. 근데 다음번에 AI가 그
코드를 다시 읽으려고 하면 자기가
만든 미로인데 자기가 못 찾아요.
의존성도 못 따라가고 어떤 모듈이 뭐
하는 건지도 모르고 결국 잘못된 모듈
고치고 다른 데서 터지는 거죠.이
이정에서 빠져나온 처방이 포코의 또
다른 스킬이에요. 인프루브 코드
베이스 아키텍처 관련된 코드들을
묶어서 하나의 뒷 모듈로 변환해요.
입구는 단순하고 안쪽은 깊은 구조로이
변환을 반복 가능한 단계로 만들어
놨다고 합니다.이 부분이 발표에서
가장 강력한 진단이라서 포코의 발표를
그대로 한번 보시죠. 슬라이드
다이어그램까지 같이 보시면 진짜 잘
와닿 거예요.
Lots of
functionality hidden
behind a simple
interface hiding the
complexity
inside the deep
module if you want
to but you don't
need to. You can
just use the
interface shallow
modules not much
functionality
complex interface
and I just wait if
you did take the
photos.
Shallow modules in a
case can of look
like this where you
have a ton of
different tiny
little blobs that
the AI has to walk
through and
navigate. And this
is really hard for
the AI to explore
actually. And so
often what you'll
see is if you have a
codebase like this,
which AI is really
good at creating
code bases like
this, is that you'll
have a situation
where AI doesn't
understand what your
code is doing. it
will attempt to
explore the code,
but because it's
poorly laid out
filled with shallow
modules, it doesn't
maybe get to the
right module in time
or doesn't
understand all the
dependencies, all
that stuff. It
doesn't understand
your code. And so
what does a codebase
full of deep modules
look like? Well,
looks like this
where it's the same
code, but it's just
structured inside
boundaries where you
have these
interfaces on the
top.
And these interfaces
you should probably
have a lot of
control over them
and design them
really well.
Otherwise, you know,
AI might mess up the
design. But the
implementation, you
can kind of leave
that to the AI a
bit.
So, how do you turn
a codebase that
looks like this into
a codebase that
looks like that?
Well, I've got a
skill for that.
Improve codebase
architecture. Turns
out this is not it's
quite complicated to
do this, but it's a
like a set of steps
that you can
reusably do again
and again. You just
sort of explore the
code base, look for
opportunities where
there's code that's
kind of um related
and wrap all of that
in a deep module.
다섯 번째 함정. 이건 진짜 다들
공감할 거예요. AI 덕에 코드 양이
폭증하잖아요. 근데 사람 머리가 못
따라가요. 폭 본인도 무대에서
솔직하게 인정해요. 내 개발자
인생에서 역대급으로 피곤하다. 본인도
지친다고요. 처방이 그레이박스
전략이에요. 회색 상자 아니 안
보이는 상자란 뜻이죠. 아까 만든 딥
모질 있잖아요. 그걸 회색 상자로
취급하는 거예요. 인터페이스는 사람이
직접 설계하고 안쪽 구여은 AI한테
통째로 위임. 사람은 인터페이스
단위로만 검증하고요. 단, 금융처럼
크리티컬한 모듈은 예외예요. 그건
안쪽까지 다 봐야 하고요. 일반
비즈니스 로직은 회색 상자로
충분하다는 거죠. 한 줄로 정리하면
이거예요. 인터페이스를 설계하라.
구현은 위임하라. 이게 펀더멘터인
동시에 AI 시대 생존 전략이라는
거죠. 자, 그래서이 여섯 가지를
관통하는 한 줄이 뭐냐? 캔트백이라는
또 다른 거장이 한 말이에요. 매일
시스템 설계에 투자하라. 이게
핵심이에요. 근데 스펙스 2 코드는
정확히 그 반대를 해요. 디자인에
투자하는게 아니라 디자인에서
디스인베스트 하는 거예요. 그래서
망한다는 거죠. 그리고이 발표에서
진짜 와닿는 마지막 비유 하나.
AI는 현장의 병장. 너는 전략가.
무슨 말이냐면 AI는 코드 변경을
직접 만드는 현장 병장이에요. 전술
단위. 근데 그 위에 누군가 있어야
한다는 거예요. 전략 수준에서
생각하는 사람. 그게 바로 더고.
그리고 전략가의 무기는 새로 산
도구가 아니라 20년 동안 쌓인
펀더멘탈이라는 거죠. 이게 41만
뷰의 진짜 이유라고 봐요.이 한
마디는 본인 톤으로 들으셔야 와닿요.
포코 본인 발표를 그대로 보시죠.
And this is the core
of it, right?
Because specing
in the design of the
system we are
divesting from it.
We're getting rid of
that. Whereas this I
think is absolutely
key.
And so code is not
cheap. That's the
message I want you
to take away. Code
is important.
If we think about AI
as a really great on
the ground
programmer, a kind
of tactical
programmer, a
sergeant on the
ground making the
cochanges, you need
someone above that.
You need someone
thinking on the
strategic level and
that's
requires software를
다시 한 주씩만 회상해 볼게요. 1.
의도가 안 맞으면 그림 위로 100번
신무시켜라. 2. AI가 장황하면
유비코터스 랭귀지로 같은 단어를 쓰게
해라. 3. 안 돌아가면 TDD로
헤드라이트보다 빨리 달리지 마라.
4. 테스트가 어려우면 딥 모듈로
구조를 다시 자라. 5. 회가 못
따라가면 그레이 박스로 위임해라.
6. 그리고 관통하는 한 줄 매일
설계에 투자해라. 전부 새로운게
아니에요. 다 옛날 책에 있는
거예요. 근데 AI 시대일수록 더
강력해지는 거고요. 저는이 발표에서
가장 강력한 한 마디가 이거였어요.
새로운 도구가 너의 무기가 아니다.
20년 동안 쌓인 펀더멘탈이 너의
무기다. 이게 제가이 채널에서 계속
얘기하고 있는 그 메시지랑 정확히
일치해요. AI 시대 생존 가이드.
그 가이드의 핵심은 결국 옛날
펀더멘탈이라는 거. 근데 오늘 제가
해드린 건 핵심 정리예요. 폭 본인의
톤, 청중 반응. 그가 무대에서
보여준 슬라이드까지 다 포함해서
18분짜리 원본을 그대로 보시면 훨씬
좋습니다. 본문에 원본 링크
첨했어요. 포콕이 만든 여섯 가지
스킬도 기터브 매트 포시 스킬스에 다
올라와 있으니까 직접 가져다 쓰셔도
됩니다. 여러분은 여섯 가지 중에
어떤게 제일 와닿으셨나요? 댓글로
알려 주세요. 그리고 좋아요와 구독은
제가이 채널을 계속 운영할 수 있는
힘이 됩니다.