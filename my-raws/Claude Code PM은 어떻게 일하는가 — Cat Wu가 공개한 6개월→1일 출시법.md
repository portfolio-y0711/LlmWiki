# Claude Code PM은 어떻게 일하는가 — Cat Wu가 공개한 6개월→1일 출시법

기획서를 거의 안 씁니다. 출시
주기는 6개월에서 하루로 줄였습니다.
PM이 직접 코드를 커밋합니다.
엔트로픽의 클로드 코드 팀
이야기예요. 엔트로픽 클로드 코드의
헤드 오브 프로덕트인 캐두가 어제
60분짜리 인터뷰에서 엔트로픽이
어떻게 일하는지를 자세하게
소개했습니다. 오늘은 그 인터뷰의
핵심만 정리합니다. 기능을 매일
출시하는 클로드 팀이 어떻게 일하는지
AI 시대의 PM의 역할이 어떻게
바뀌고 있는지 그리고 클로드를
누구보다 많이 쓰는 클로드 팀의
PM은 AI가 사람을 대치할 수
있다고 보는지이 세 가지로
정리합니다. 먼저 한번 봅시다.
진짜로 그렇게 빠르긴 한 건지. 올해
1월부터 3월까지 90일 동안
엔트로픽이 출시한 기능이
35개입니다. 모델, 제품, 클로드
코드, 엔터프라이즈, 플랫폼 다
합쳐서요. 평균 2.61에 하나씩
출시한 셈이에요. 일반적인 회사가
가능한 속도가 아니죠. 레니스
팟캐스트의 진행자도 인터뷰 첫
머리에서 이렇게 말합니다. 이런
페이스는 본 적이 없다고요. 매일
메이저 기능이 나오고 있다고. 우는
그 비결을 인터뷰에서 직접 이렇게
말했습니다. 예전에
slower
12 months.
And because
shiatures of slower
rate, there was a
lot more emphasis on
coordinating with
all the other
partner teams to
make sure that their
shipping features
that unblock your
features because
code at that time
was very expensive
to make. I think now
with AI and with how
much that has
accelerated
engineering and with
how quickly the
model capabilities
are improving the
timelines
of our productes
gone down from month
to one month and
sometimes
6개월 걸리던 기능이 지금은 하루
만에 나옵니다. 근데 진짜 궁금한 건
이거예요. 어떻게요? 캔우의 첫 번째
답은 단순합니다. 프로세스를 거의 다
없앴다는 거예요. 본인 표현 그대로
옮기면 프로세스는 최소한으로 가져가고
출시의 모든 장벽을 없앤다는
말이에요. 근데 프로세스가 없다는게
구체적으로 뭐냐? 세 가지로
정리됩니다. 첫 번째 기획서를 거의
안 씁니다. 해외에서 PRD라고
부르는 제품 요구 사항 말이에요.
보통 회사라면 PM이 이걸 쓰고
결제받고 디자인 팀에 넘기고 개발
팀에 넘기죠. 출시, 클로드 코드
팀은 이걸 안 합니다. 대신 두
가지가 그 자리를 대신해요. 하나는
매주, 매트릭, 리뷰. 모든 팀원이
회사가 어떻게 굴러가는지 숫자로 같이
봅니다. 다른 하나는 팀 원칙 문서.
우리의 핵심 사용자가 누구인지, 왜
그들이 우리 핵심 사용자인지를
문서화해 놔요.이 두 개가 있으면
PM 결제 없이도 누구든 결정할 수
있어요. PM이 병목이 안 됩니다.
두 번째 역할 구분이 모해졌습니다.
PM이 직접 코드를 밋밋하고
디자이너가 프론트엔드를 짜고
엔지니어가 PM를 합니다. 캣 우운
자기 팀의 디자이너들도 거의 다
프론트엔드 엔지니어 출신이라고
말했어요. 세 번째 채용부터
다릅니다. 코드 PM을 더 뽑기보다
프로덕트 테이스트 있는 엔지니어를 더
많이 뽑는 전략이에요. 본인도
엔지니어 출신이고 팀의 PM 대부분이
엔지니어였거나 지금도 클로드 코드에서
직접 코드를 짭니다.이 세 가지가
합쳐지면 어떻게 되는가? 누군가
아이디어를 내면 그 사람이 직접
만들어서 일주일 안에 시장에 내놓을
수 있어요. PM 결제도 디자인
핸드오프도 개발팀 인계도 없으니까요.
근데이 빠른 출시에는 또 하나의
비밀이 있어요. 어떻게 마음 편하게
빨리 내놓을 수 있느냐. So for
what do we actually
ship almost all our
features in research
preview clearly
brand this um when
we ship something so
that users know that
this is an early
product. This is
just an idea. This
is just something
that we're trying to
get feedback on and
iterating on. And
that this might not
be supported
forever.
이게 마음편이 빨리 내놓을 수 있는
또 하나의 장치예요. 리서치
프리뷰라는 라벨 하나로 사용자한테
미리 약속해 두는 거죠. 이건 아직
실험이고 안 좋으면 사라질 수도
있다고요. 그러면 팀도 부담이 줄고
사용자도 기대치를 거기에 맞추게
됩니다. 기획서 폐기, 역할 모호,
코드자는 PM 채용, 그리고 리서치
프리뷰 브랜드.이 네가 가지가
합쳐져서 6개월짜리 일이 하루로
줄어드는 거예요. 근데 프로세스를 다
없애도 회사가 굴러가야 정상이잖아요.
누가 결정을 내려요? 어떻게 방향이
안 어긋나죠? 여기서 캣 우우가 던진
답이이 인터뷰에서 가장 중요한
부분이라고 봅니다. 프로세스를 없앨
수 있는 진짜 이유는 미션이 의사
결정에 디폴트를 만들어 주기
때문이라는 거예요. 쉽게 풀면 두
가지 우선 순위가 충돌할 때마다 어느
쪽이 우리 미션에 더 가까운가로
직결한다는 뜻이에요. 회의도 토론도
정치도 필요 없습니다. 같은 기준이
모두 머릿속에 있으니까요. 엔트로픽의
미션은 단순해요. 안전한 Agi를
인류에게 가져다 주자. 근데 이게
추상적인 말로만 끝나지 않는다는게
핵심이에요. 겟우는 인터뷰에서 직접
이런 말까지 했습니다.
Mission means that
teams are willing to
make sacrifices that
hurt their own goals
and their owns in
service of anthropic
goals and anthropics
koss. And
people are very
happy to make those
tradeofs. So like an
extreme example is
if Code failed but
Anthropic succeeded
I would be extremely
happy and like the
whole team is very
decisions
that
>> 표현으로는 extreme
example이라고 단서를 달았어요.
단정이 아닌 사고실험 차원의
발언이에요. 그 단서까지 포함해서
들으면 의미는 이렇게 됩니다. 만약
클로드 코드가 실패하더라도 회사 전체
미션이 더 중요하면 그쪽을 선택할 수
있다는 거예요. 보통 한 제품의
헤드가 이렇게 말하기는 어렵습니다.
그 제품이 본인 자리니까요. 제품
우선 순위가 회사 미션보다 위에 갈
수 없다는 사고 방식이 팀 전체에
깔려 있다는 뜻이에요. 이런 사고
방식이 팀 전체에 깔려 있으면 어떤
결정이든 길게 끌 일이 없어져요.
클로드 코드 입장에선 이게 좋지만
엔트로픽 전체로는 저게 맞다 그러면
저쪽으로 갑니다. 토론이 길어지지
않아요. 같은 기준이 머릿속에 있으니
절차로 일일이 정하지 않아도 결정이
나옵니다. 프로세스를 없앨 수 있었던
진짜 배경이에요. 물론이 속도가
공짜는 아닙니다. 캐우도 인터뷰에서
솔직하게 인정했어요. 빠르게 출시한
대가로 이은게 있다고. 가장 큰 건
제품의 일관성입니다. 같은 일을 할
수 있는 기능이 두 세 개씩 동시에
존재해요. 어떤게 베스트 프랙티스인지
사용자가 알 수 없는 거예요. 캔우
우표으로는 일관성을 시장에 위임한
셈이라고 했습니다. 사용자들이 직접
써 보고 어느게 더 나은지 알려주면
그걸 보고 정리한다는 거죠. 또 하나
흥미로운 건 새 모델이 나올 때마다
기존 기능을 지운다는 거예요. 예를
들어 초기에는 클로드가 큰 작업을
하다가 중간에 잊어버려서 투 리스트
기능을 따로 붙여 놨대요. 근데
모델이 강해지니까 알아서 투를 만들고
알아서 따라가요. 그 기능은 더 이상
강조하지 않아요. 모델이 자기가 만든
도구를 잡아 먹는 셈이에요. 빠르게
만들면 빠르게 지웁니다. 안정성보다
시장 피드백을 우선한 결과예요. 근데
이게 회사 차원 얘기였잖아요. 그
안에서 일하는 PM 한 명은 도대체
어떻게 일할까요?
터뷰에서 PM의 핵심 능력으로 가장
강조한 건 프로덕트 데이스트예요.
우리 말로 옮기면 제품 감각 또는
무엇을 만들지에 대한 안목 정도가
됩니다. 본인 입으로 직접 이렇게
말했어요. I still think
it comes back to
product like as code
becomes much cheaper
to write the thing
that becomes more
valuable is deciding
what to write. Like
what is the right UX
for this feature?
What is the most
delightful way that
a user can
experience it? What
like we we get tens
of thousands of
GitHub issues asking
for every single
thing under the sun
and it takes a lot
of care and taste to
figure out which of
these is worth
building and what is
the right way to
build it. And I
think that skill can
come from any
background
생각해 보면 당연한 얘기예요. AI가
코드를 짜주니까 코드 자체는
싸졌어요. 그러면 가치는 다른 데로
옮겨 가요. 어떻게 만들지에서 무엇을
만들지로요. 캐도는 매일 키터브에
수만 개의 기능 요청이 올라온다고
했어요. 그중에 진짜 만들어야 할게
어느 것인지 어떻게 만들어야 사용자가
가장 행복할지 이걸 판단하는게 PM의
진짜 일이에요. 이게 학교에서 가르쳐
주는 일이 아닙니다. 자격증으로
증명되는 것도 아니에요. 수많은
사용자 피드백을 보고 직접 도구를
매일 써 보고 모델의 한계를 손으로
익혀야 길러지는 감각이에요. 케두가
인터뷰에서 가장 어렵다고 한 스킬이
따로 있어요. 1개월 후 제품이
어떻게 보여야 하는지 정의하는 것.
이게 무슨 말이냐? AI 모델은 매달
능력이 바뀝니다. 사용자 행동도 매달
바뀌어요.이 모호한 환경에서 한 달
뒤를 그릴 줄 알아야 한다는 거예요.
케두는 이걸 AGI 필드의 적정선
찾기라고 표현했어요. 너무 AGI를
신봉하면 제품이 그냥 텍스트 박스
하나로 단순해집니다. 어차피 모델이
알아서 다 해 주니까 뭘 만들 필요
없잖아. 근데 현재 모델은 그렇게 못
해요. 그래서 제품이 안 굴러가요.
반대로 AGI를 너무 안 믿으면 현재
모델 한 개만 보고 보수적으로
짭니다. 6개월 뒤에 모델이 좋아지면
쓸모 없어져요. 여기서 캣우가
인터뷰에서 한 가장 빛나는 한 마디가
나옵니다. 미래의 슈퍼 AGI용
제품을 만드는 건 정말 쉽다. 진짜
어려운 건 지금 모델의 능력을 최대로
끌어내는 제품을 만드는 것이다. 좋은
PM은이 다이어를 한 번 맞추는게
아니라 새 모델이 나올 때마다 다시
맞춰야 합니다. 모델 능력이 예상보다
좋으면 길을 바꾸고 예상보다 나쁘면
또 길을 바꿔요. 이게 정답이 없는
일이에요. 그래서 가장 어려운 거고
그래서 가장 비싼 능력이 됩니다.
이게 클로드 코드 PM이라는
방식입니다. 무엇을 만들지에 대한
감각이 있고 지금 모델로 굴러가는
제품을 그릴 줄 알면서 모델이 바뀔
때마다 그 다이어를 다시 맞출 줄
아는 사람. 근데이 인터뷰에서 가장
흥미로웠던 부분은 사실 여기서 한 발
더 나간 질문이었어요. 레니가 캣
우우이에게 직접 물어봅니다. 초지능이
오기 전까지 사람의 두뇌가 계속
필요한 영역은 어디일까요?
클로드코드의 헤드 프로덕트가이 질문에
어떻게 답할지 한번 들어보세요.
at least
I think humans still
provide a level of
common sense that
the models don't
and there's like
moving pieces to any
product launch some
of them are very
small but there's
always a lot that
could potentially go
wrong I think the
model doesn't always
have a great sense
of who all the
stakeholders are how
they relate to each
other what their
preferences
EQ
>> 모델이 갖지 못한 수준의 상식
커먼스를 사람이 제공한다는 거예요.
겟 우가든 예시가 직관적이에요. 제품
하나를 출시하려면 거기에
1천000개쯤 되는 움직이는 부품이
있어요. 누가 영향 받는지, 누구한테
미리 알려야 하는지, 누구를 어떻게
설득해야 하는지. 케두는 PM이 매일
하는이 일을 모델이 도와주지 못한다고
말했어요. 구체적으로 내 영역을
짚었습니다. 하나. 이해 관계자.이
이 출시가 회사 안에서 누구에게
영향을 주는지 모델이 알아내기
어려워요. 영업 팀이 영향 받는지,
디자인 팀이 영향 받는지, 외부
파트너까지 챙겨야 하는지. 둘, 관계
구조. 그 사람들이 서로 어떻게 엮겨
있는지 모릅니다. A 팀장과 B
팀장이 친한 사이인지, 이전에 무슨
일이 있었는지. 셋, 개인 선호. 각
사람이 무엇을 좋아하고 무엇을 거슬려
하는지 모릅니다. 어떤 사람은
이메일로 보고 받는 걸 선호하고 어떤
사람은 회의 자리에서 세 소식 듣는
걸 싫어해요. 넷. 소통 채널.
그래서 누구한테 언제 어떤 자리에서
알려야 출시가 매끄럽게 굴러가는지
판단을 못 합니다. PM이 매일 하는
그 판단이에요. 문서에 적히지 않은
인간 사회의 운영 규칙이에요. 캣우는
이걸 안목적 상식과 EQ적 지식이라고
표현했어요. 근데 캣 5는
솔직했어요. 마지막에 단서를
달았거든요. 이것도 결국 모델이 더
잘하게 될 겁니다. 하지만 지금은
아직 사람 영역이에요. 이게이
인터뷰에서 가장 중요한 단서라고
봅니다. 연구적 우이가 아니라 지금의
우위라는 거. 그래서 살아남는 사람은
지금이 자리를 차지한 사람이 아니라
갭이 어디로 옮겨가든 빠르게 따라가는
사람이에요. 원본 인터뷰는
60분짜리예요. 영상 설명란 첫 줄에
링크 달아 놨습니다. 영어 듣기 부담
없으시면 꼭 한번 직접 보시는 걸
추천드립니다. 오늘은 여기까지입니다.