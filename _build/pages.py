"""Build the O Tse & Co. concept site (no dependencies).

    python3 _build/pages.py && python3 _build/fonts.py

English at /, Traditional Chinese at /zh/. Every string is written as L(english, chinese).
"""
import json
import os
import urllib.parse

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
V = "5"  # cache-bust: bump on every CSS/JS change

LANG = "en"


def L(en, zh):
    return en if LANG == "en" else zh


# ------------------------------------------------------------------ facts (source: otse.co.uk, November 2026)
PHONE = "0161 923 4667"
TEL = "+441619234667"
WA_SHOW = "07511 374988"
WA = "447511374988"
EMAIL = "ask@otse.co.uk"
ADDR = "Unit 3F01, Oxford Place, 61 Oxford Street, Manchester M1 6EQ"
OFFICIAL = "https://otse.co.uk/"
UXC = "https://ux-circles.com/professionals"
HOME = [-2.2421238, 53.4759435]
BASE = "https://uxcircles.github.io/otse/"
ROUTES = json.load(open(os.path.join(BUILD, "routes.json")))
STATIONS = [
    ("Oxford Road", "Manchester Oxford Road station", "曼徹斯特 Oxford Road 火車站"),
    ("St Peter's Square", "St Peter's Square tram stop", "St Peter's Square 電車站"),
    ("Piccadilly", "Manchester Piccadilly station", "曼徹斯特 Piccadilly 火車站"),
]

PX = ""  # prefix to the site root ("" or "../")


def wa(msg):
    return f"https://wa.me/{WA}?text=" + urllib.parse.quote(msg)


def mark(cls="mark", white=False):
    return f'<img class="{cls}" src="{PX}assets/img/mark{"-white" if white else ""}.svg" width="70" height="70" alt="" aria-hidden="true">'


def tiles(cls=""):
    """The two-tile divider: the logo mark drawn in CSS."""
    return f'<div class="tiles {cls}" aria-hidden="true"><i></i><i></i></div>'


# ------------------------------------------------------------------ chrome
NAV = [
    ("personal.html", "Personal", "個人服務"),
    ("business.html", "Business", "商業服務"),
    ("cases.html", "Cases", "成功案例"),
    ("about.html", "About", "關於我們"),
    ("contact.html", "Contact", "聯絡我們"),
]


def other_lang(slug):
    s = "" if slug == "index.html" else slug
    if slug == "404.html":
        return BASE + ("zh/" if LANG == "en" else "")
    return ("zh/" + s) if LANG == "en" else ("../" + s)


def head(slug, title, desc):
    s = "" if slug == "index.html" else slug
    return f'''<!doctype html>
<html lang="{L('en-GB', 'zh-Hant-HK')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="en" href="{BASE}{s}">
<link rel="alternate" hreflang="zh-Hant" href="{BASE}zh/{s}">
<link rel="icon" type="image/svg+xml" href="{PX}assets/img/favicon.svg">
<meta name="theme-color" content="#2a3b6f">
<link rel="preload" href="{PX}assets/fonts/familjen.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{PX}assets/fonts/{L('onest', 'chiron-sung-700')}.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{PX}assets/site.css?v={V}">
<script defer src="{PX}assets/site.js?v={V}"></script>
</head>
'''


def header(slug):
    links = "".join(
        f'<a href="{h}"{" aria-current=page" if h == slug else ""}>{L(en, zh)}</a>' for h, en, zh in NAV
    )
    sw = L("中文", "English")
    swl = L("zh-Hant", "en")
    return f'''<body class="pg-{slug.replace('.html', '')}">
<a class="skip" href="#main">{L("Skip to content", "跳至內容")}</a>
<div class="concept-bar" role="note">
  <div class="wrap concept-inner">
    <p><span class="concept-tag">{L("Concept", "概念")}</span><span class="concept-long">{L('Redesign concept. Not the <a href="' + OFFICIAL + '" target="_blank" rel="noopener">official O Tse &amp; Co. website</a>.', '改版概念設計，並非 <a href="' + OFFICIAL + '" target="_blank" rel="noopener">謝延豐律師行官方網站</a>。')}</span></p>
    <a href="{UXC}" target="_blank" rel="noopener"><span class="concept-by">Designed by </span><strong>UX CIRCLES</strong> <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></a>
  </div>
</div>
<header class="head" id="top">
  <div class="wrap head-in">
    <a class="brand" href="index.html" aria-label="{L('O Tse &amp; Co., home', '謝延豐律師行 首頁')}">
      {mark("brand-mark")}
      <span class="brand-txt"><span class="brand-en">O Tse &amp; Co.</span><span class="brand-zh" lang="zh-Hant">謝延豐律師行</span></span>
    </a>
    <nav class="nav" aria-label="{L('Main', '主選單')}">{links}</nav>
    <a class="lang" href="{other_lang(slug)}" lang="{swl}" hreflang="{swl}">{sw}</a>
    <a class="head-call" href="tel:{TEL}">{PHONE}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">{L('Menu', '選單')}</button>
  </div>
  <div class="menu" id="menu" hidden>
    <nav class="wrap" aria-label="{L('Menu', '選單')}">
      {links}
      <a href="{other_lang(slug)}" lang="{swl}">{sw}</a>
      <a href="tel:{TEL}">{L('Call', '致電')} {PHONE}</a>
    </nav>
  </div>
</header>
<main id="main">
'''


def mbar(slug):
    msg = L("Hello, I would like to book a first consultation.", "你好，我想預約首次諮詢。")
    return f'''<nav class="mbar" aria-label="{L('Quick actions', '快捷操作')}">
  <a href="tel:{TEL}"><span class="mb-ic mb-call" aria-hidden="true"></span>{L('Call', '致電')}</a>
  <a href="{wa(msg)}" data-wa><span class="mb-ic mb-wa" aria-hidden="true"></span>WhatsApp</a>
  <a href="{'#ask' if slug in ('index.html', 'contact.html') else 'contact.html#ask'}"><span class="mb-ic mb-ask" aria-hidden="true"></span>{L('Ask', '查詢')}</a>
</nav>'''


def footer(slug):
    links = " · ".join(f'<a href="{h}">{L(en, zh)}</a>' for h, en, zh in NAV)
    return f'''</main>
<footer class="foot">
  <div class="wrap foot-grid">
    <div class="foot-id">
      {mark("foot-mark", white=True)}
      <p class="foot-name">O Tse &amp; Co. Limited<br><span lang="zh-Hant">謝延豐律師行</span></p>
      <p>{ADDR}</p>
    </div>
    <div>
      <p><a href="tel:{TEL}">{PHONE}</a> · {L('office', '辦公室')}</p>
      <p><a href="https://wa.me/{WA}">{WA_SHOW}</a> · WhatsApp</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>{L('Monday to Friday, 9:30am to 5:30pm', '星期一至五 上午9:30 至 下午5:30')}</p>
    </div>
    <div>
      <p>{links}</p>
      <p><a href="privacy.html">{L('Privacy and accessibility', '私隱及無障礙')}</a> · <a href="{other_lang(slug)}" lang="{L('zh-Hant', 'en')}">{L('中文', 'English')}</a></p>
      <p class="foot-small">{L('Regulated by the Solicitors Regulation Authority. Information on this site is general and is not legal advice.', '受英國律師監管局（SRA）規管。本網站內容只屬一般資訊，並非法律意見。')}</p>
      <p class="foot-small">{L('Unofficial redesign concept by', '非官方概念設計：')} <a href="{UXC}" target="_blank" rel="noopener">UX CIRCLES</a></p>
    </div>
  </div>
</footer>
{mbar(slug)}
</body>
</html>
'''


def page(slug, title, desc, body):
    return head(slug, title, desc) + header(slug) + body + footer(slug)


# ------------------------------------------------------------------ shared blocks
def open_status():
    return f'<p class="status" data-open><span class="status-dot" aria-hidden="true"></span><span data-open-txt>{L("Monday to Friday, 9:30am to 5:30pm", "星期一至五 上午9:30 至 下午5:30")}</span></p>'


PERSONAL = [
    ("conveyancing", "Conveyancing and land law", "樓宇買賣及土地法",
     "Buying or selling a home, from a first flat to a chain of several sales, and land disputes and development agreements.",
     "由首次置業到牽涉多宗買賣的連鎖交易，以及土地糾紛和發展協議。"),
    ("tenancy", "Landlord and tenant disputes", "業主與租客糾紛",
     "Protecting your rights as either a landlord or a tenant, aiming for a resolution that respects everyone's legal rights.",
     "保障您作為業主或租客的權利，達成尊重各方法律權益的解決辦法。"),
    ("wills", "Wills and probate", "遺囑及遺產認證",
     "Clear, valid wills, estate administration and probate, and inheritance disputes, handled with care.",
     "起草清晰有效的遺囑，處理遺產管理、遺產認證及繼承糾紛。"),
    ("family", "Family law", "家庭法",
     "Divorce, child arrangements, maintenance and property settlements, resolved amicably where possible.",
     "離婚、子女安排、贍養費及財產分配，盡可能以和解方式處理。"),
    ("employment", "Employment law", "勞工法",
     "Wrongful dismissal, contract problems and workplace injury, for employees who want fair treatment.",
     "不當解僱、合約問題及工傷，確保您在工作場所得到公平對待。"),
    ("dispute", "Litigation and dispute resolution", "訴訟與爭議解決",
     "Personal disputes resolved through negotiation, mediation or court, with your interests protected at each step.",
     "以談判、調解或訴訟解決個人糾紛，每一步都保障您的利益。"),
    ("defamation", "Defamation", "誹謗",
     "Slander or libel, online or offline: protecting your reputation and restoring your standing.",
     "無論是口頭或書面、網上或網下的誹謗，維護您的名譽。"),
    ("nuisance", "Nuisance", "滋擾",
     "Noise, pollution and other disturbances from neighbours or businesses, dealt with through legal channels.",
     "鄰居或商戶造成的噪音、污染及其他滋擾，循法律途徑處理。"),
]

BUSINESS = [
    ("commercial", "Commercial law", "商業法",
     "Contracts, transactions and regulatory compliance, so the business runs smoothly and on a sound legal footing.",
     "合約、交易及法規遵從，令業務順利並合法運作。"),
    ("corporate", "Corporate law", "公司法",
     "From forming a company to governance and growth: structures that keep you within the rules.",
     "由成立公司到公司管治及擴展，確保公司符合法規。"),
    ("employer", "Employment law for employers", "僱主勞工法",
     "Employment contracts, staff policies, advice on rights and obligations, and defending disputes.",
     "起草僱傭合約及員工政策，就權利義務提供意見，並在爭議中為您辯護。"),
    ("commercial-lease", "Commercial landlord and tenant", "商業租務糾紛",
     "Disputes over commercial premises, mediated or litigated, for owners and tenants alike.",
     "商業物業的業主與租戶糾紛，以調解或訴訟處理。"),
    ("business-dispute", "Business disputes", "商業爭議",
     "Litigation or alternative dispute resolution that keeps risk and disruption to the business low.",
     "以訴訟或另類排解程序解決商業爭議，將風險及對業務的影響減到最低。"),
]


def area_list(items, tone):
    return '<ul class="areas areas-' + tone + '">' + "".join(
        f'<li id="{k}"><h3>{L(en, zh)}</h3><p>{L(den, dzh)}</p></li>' for k, en, zh, den, dzh in items
    ) + "</ul>"


CASES = [
    ("workplace-injury", "Employment", "勞工法", "22 September 2024", "2024年9月22日",
     "Workplace injury: a fair settlement after the employer said no", "工傷：僱主拒絕賠償後，取得公平和解",
     ["The client, an employee at a manufacturing company, was injured at work because of inadequate safety measures. Her employer dismissed her concerns and was reluctant to provide suitable compensation, leaving her stressed and unsure of her rights.",
      "We advised her on her legal rights and reviewed her employment conditions, the company's safety protocols and the circumstances of the injury. With the evidence gathered, we negotiated firmly with the employer for fair compensation and the medical care she needed.",
      "We secured a settlement that covered her medical expenses and compensated her for pain and suffering, so she could focus on her recovery."],
     ["客戶是一間製造公司的員工，因公司安全措施不足而在工作中受傷。僱主起初否認責任，亦不願作出適當賠償，令客戶承受壓力，也不清楚自己的權益。",
      "我們就她的法律權利提供意見，並全面審視她的僱傭條件、公司的安全守則及受傷經過。收集足夠證據後，我們與僱主據理力爭，為她爭取公平賠償及所需的醫療照顧。",
      "最終我們取得和解，賠償涵蓋她的醫療開支及傷痛損失，讓她可以專心康復。"]),
    ("property-chain", "Conveyancing", "樓宇買賣", "1 September 2024", "2024年9月1日",
     "A house sale in a chain, completed on time", "連鎖交易中的賣樓，按時完成",
     ["Our client was selling a house that sat in a chain of several buyers and sellers. Deadlines were tight and the chain was at risk of collapsing.",
      "We coordinated with the solicitors for every other party in the chain, carried out due diligence early to catch problems before they arose, and prepared the documents in advance.",
      "By keeping communication open and negotiating carefully, we lined up the completion dates across the chain. The client sold on time."],
     ["客戶出售的房屋處於一條牽涉多名買家及賣家的連鎖交易之中，期限緊迫，整條交易鏈隨時可能斷裂。",
      "我們與交易鏈中各方的律師協調，及早進行盡職審查以預先發現問題，並提前備妥所需文件。",
      "透過保持溝通及審慎談判，我們令整條交易鏈的成交日期一致，客戶最終按時賣出房屋。"]),
    ("estate", "Probate", "遺產認證", "22 August 2024", "2024年8月22日",
     "An estate with many assets and debts, settled for the family", "資產與債務繁多的遺產，為家人妥善處理",
     ["After his father died, our client was left with a complex estate of multiple assets and outstanding debts. The family did not know the legal procedures and were grieving.",
      "We took on the probate and estate administration: valuing the estate, settling debts and distributing the assets according to the will. Where beneficiaries disagreed, we helped them talk it through and mediated.",
      "The family had regular updates throughout. The estate was settled efficiently and the family could move on."],
     ["客戶的父親離世後，留下一筆包括多項資產及未清債務的複雜遺產。家人不熟悉法律程序，同時承受喪親之痛。",
      "我們接手遺產認證及遺產管理：為遺產估值、清還債務，並按遺囑分配資產。受益人之間出現分歧時，我們協助溝通並進行調解。",
      "整個過程中我們定期向家人匯報進度。遺產得以順利處理，家人亦可以放下心頭大石。"]),
]


def case_cards(link=True):
    out = []
    for k, en_t, zh_t, en_d, zh_d, en_h, zh_h, en_p, zh_p in CASES:
        tag = L(en_t, zh_t)
        h = L(en_h, zh_h)
        first = L(en_p, zh_p)[0]
        href = f"cases.html#{k}"
        out.append(f'''<article class="case-card">
  <p class="case-meta"><span>{tag}</span> <time>{L(en_d, zh_d)}</time></p>
  <h3><a href="{href}">{h}</a></h3>
  <p>{first}</p>
</article>''')
    return '<div class="case-cards">' + "".join(out) + "</div>"


TESTI = {
    "tam": ("Property purchase", "樓宇買賣", "Mrs Tam", "譚女士",
            "During the purchase of our new home, the team demonstrated exceptional diligence and expertise. Every step felt streamlined and secure thanks to their meticulous attention to detail and proactive communication.",
            "在購買新家的過程中，團隊展現了非凡的勤奮和專業。由於他們對細節的關注和積極的溝通，每一步都顯得流暢而安全。"),
    "lee": ("Probate", "遺囑認證", "Mr Lee", "李先生",
            "After the passing of my father, the thought of dealing with legal matters seemed overwhelming. The team handled my father's estate with such professionalism and sensitivity that it significantly eased my burden during a difficult time.",
            "我父親過世後，要處理法律事宜令我感到不知所措。團隊以專業而體貼的方式處理父親的遺產，在困難時期大大減輕了我的負擔。"),
    "chan": ("Family law", "家庭法", "Mr Chan", "陳先生",
             "Going through a divorce is never easy, but the support and guidance I received were outstanding. They worked tirelessly to ensure a fair settlement and kept in touch throughout.",
             "經歷離婚絕非易事，但我得到的支持和指導非常出色。他們不懈努力確保達成公平的和解，並在整個過程中保持良好溝通。"),
    "chu": ("Commercial law", "商業法", "Mr Tom Chu", "Mr Tom Chu",
            "Their expertise in commercial law helped us navigate complex transactions smoothly and kept us compliant with changing regulations.",
            "他們在商業法方面的專業，幫助我們順利處理複雜的交易，並確保我們遵守不斷變化的法規。"),
    "chen": ("Litigation", "訴訟", "Mrs Chen", "陳女士",
             "They resolved a potentially costly litigation for us and managed to preserve important business relationships at the same time.",
             "他們成功解決了一宗可能代價高昂的訴訟，同時保住了重要的商業關係。"),
    "wong": ("Employment law", "勞工法", "Mr Wong", "黃先生",
             "From drafting policies that protect our company and our employees to defending us in employment disputes, their advice is always clear and actionable.",
             "由草擬保障公司和員工的政策，到在勞資爭議中為我們辯護，他們的建議總是清晰可行。"),
}


def quotes(keys, tone):
    out = []
    for k in keys:
        en_t, zh_t, en_n, zh_n, en_q, zh_q = TESTI[k]
        out.append(f'<figure class="quote"><blockquote><p>{L(en_q, zh_q)}</p></blockquote><figcaption><strong>{L(en_n, zh_n)}</strong> · {L(en_t, zh_t)}</figcaption></figure>')
    return f'''<section class="sec quotes-sec quotes-{tone}" aria-labelledby="q-h">
  <div class="wrap">
    <h2 id="q-h">{L('What clients have told us', '客戶的話')}</h2>
    <div class="quotes">{''.join(out)}</div>
    <p class="fine">{L('Published on the firm’s current website.', '摘自律師行現有網站。')}</p>
  </div>
</section>'''


FAQ = [
    ("How do I book a first consultation?", "如何預約首次諮詢？",
     f'Call the office on <a href="tel:{TEL}">{PHONE}</a>, send a WhatsApp to <a href="https://wa.me/{WA}">{WA_SHOW}</a> with a short description and the times that suit you, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.',
     f'致電辦公室 <a href="tel:{TEL}">{PHONE}</a>；或以 WhatsApp <a href="https://wa.me/{WA}">{WA_SHOW}</a> 簡述您的問題及方便的時間；或電郵至 <a href="mailto:{EMAIL}">{EMAIL}</a>。'),
    ("How should I prepare?", "首次諮詢前應如何準備？",
     'Gather the documents related to your matter, and write a short timeline of what happened. Think about what you want to achieve. The <a href="contact.html#prepare">first-meeting checklist</a> lists what to bring for the common matters.',
     '收集與事件相關的文件，並寫下簡單的事件時序，想清楚您希望達到的結果。<a href="contact.html#prepare">首次見面清單</a>列出了常見事務需要帶備的文件。'),
    ("What will it cost?", "收費如何計算？",
     "Fees depend on the complexity of the matter and the type of work. We offer hourly rates and fixed fees, depending on the case, and give you a clear outline of the expected costs at your first consultation.",
     "費用視乎案件的複雜程度及服務類型而定。我們按個別情況提供計時收費或固定收費，並會在首次諮詢時清楚說明預計費用。"),
    ("How long will it take?", "案件通常需時多久？",
     "It depends on how complex the case is, how far the other parties cooperate and how busy the courts are. We work to resolve matters as efficiently as possible and tell you honestly when something will take longer.",
     "視乎案件的複雜程度、各方的合作程度及法院的效率而定。我們會盡量有效率地處理，需要較長時間的話也會如實告訴您。"),
    ("Can I speak Cantonese with you?", "可以用廣東話溝通嗎？",
     "Yes. The firm is fluent in Cantonese and works with many families who have moved from Hong Kong. Meetings can be in Cantonese or English, at the office on Oxford Street or by phone or video, nationwide.",
     "可以。我們精通廣東話，服務很多從香港移居英國的家庭。會面可以用廣東話或英文進行，可以到 Oxford Street 的辦公室，亦可以透過電話或視像，服務遍及全英國。"),
]


def faq():
    items = "".join(
        f'<details><summary>{L(q, qz)}</summary><p>{L(a, az)}</p></details>' for q, qz, a, az in FAQ
    )
    return f'''<section class="sec faq-sec" aria-labelledby="faq-h">
  <div class="wrap faq-grid">
    <h2 id="faq-h">{L('Questions people ask first', '大家最先問的問題')}</h2>
    <div class="faq">{items}</div>
  </div>
</section>'''


CHECK = [
    ("buy", "Buying a home", "買樓", [
        ("Passport for everyone buying", "所有買家的護照"),
        ("Proof of address from the last 3 months (bank statement or utility bill)", "最近 3 個月的住址證明（銀行月結單或水電煤賬單）"),
        ("The memorandum of sale from the estate agent", "地產代理發出的 memorandum of sale（買賣備忘）"),
        ("Mortgage offer or agreement in principle, if you have one", "按揭批核或原則上批核書（如有）"),
        ("Bank statements showing where the deposit comes from, including transfers from Hong Kong", "顯示首期來源的銀行月結單，包括由香港匯款的紀錄"),
        ("If family are gifting money: their names and how much", "如有家人贈予款項：贈予人姓名及金額"),
        ("A list of any other property you own, in the UK, Hong Kong or anywhere else", "您在英國、香港或其他地方擁有的其他物業"),
    ]),
    ("sell", "Selling a home", "賣樓", [
        ("Passport and proof of address for every owner", "每位業主的護照及住址證明"),
        ("Mortgage lender and account number", "按揭銀行及戶口號碼"),
        ("Certificates and guarantees for work done (windows, boiler, extensions)", "工程證書及保用（窗戶、鍋爐、擴建等）"),
        ("For a leasehold flat: the lease and recent service charge statements", "如屬 leasehold 單位：租約及最近的管理費結單"),
        ("Details of the buyer’s solicitor, if the sale is already agreed", "買方律師資料（如已談妥買賣）"),
    ]),
    ("tenancy", "A landlord or tenant problem", "業主與租客問題", [
        ("The tenancy agreement and any renewals", "租約及續約文件"),
        ("Deposit protection certificate", "按金保障證明（deposit protection certificate）"),
        ("Rent records: bank transfers or a rent statement", "租金紀錄：銀行轉賬或租金結單"),
        ("Every notice or letter given or received, with the date it arrived", "所有發出或收到的通知或信件，並註明收到日期"),
        ("Photos and messages about the problem", "與問題有關的相片及訊息"),
    ]),
    ("employment", "A problem at work", "工作上的問題", [
        ("Your employment contract and staff handbook", "僱傭合約及員工手冊"),
        ("Recent payslips", "最近的糧單"),
        ("Letters about the problem: dismissal, disciplinary, grievance", "相關信件：解僱、紀律處分、申訴"),
        ("A dated timeline of what happened", "附日期的事件時序"),
        ("For an injury: medical notes and any accident report", "如涉及工傷：醫療紀錄及意外報告"),
    ]),
    ("will", "Making a will or dealing with an estate", "立遺囑或處理遺產", [
        ("For a will: a list of what you own in the UK and Hong Kong (property, bank accounts, MPF, pensions)", "立遺囑：您在英國及香港的資產清單（物業、銀行戶口、強積金、退休金）"),
        ("Who you want to benefit, and who you would like as executors", "受益人及希望委任的遺囑執行人"),
        ("Guardians you would choose for children under 18", "為未滿 18 歲子女選定的監護人"),
        ("For an estate: the death certificate and the original will", "處理遺產：死亡證及遺囑正本"),
        ("Statements for the person’s accounts, property and debts", "已故者的銀行戶口、物業及債務資料"),
    ]),
    ("family", "Separation or divorce", "分居或離婚", [
        ("Marriage certificate (a Hong Kong certificate is fine)", "結婚證書（香港發出的亦可）"),
        ("Children’s birth certificates", "子女出生證明書"),
        ("An outline of income, property, savings and pensions on both sides, including MPF", "雙方收入、物業、儲蓄及退休金（包括強積金）概要"),
        ("A timeline of the separation and any court papers", "分居經過的時序及任何法庭文件"),
    ]),
    ("dispute", "A dispute, defamation or nuisance", "糾紛、誹謗或滋擾", [
        ("A dated timeline of what happened", "附日期的事件時序"),
        ("Contracts, invoices, letters and messages", "合約、發票、信件及訊息"),
        ("Screenshots showing the date and web address, for anything online", "如涉及網上內容：顯示日期及網址的截圖"),
        ("Photos, recordings or a noise diary, for a nuisance", "如涉及滋擾：相片、錄音或噪音日誌"),
        ("Any court papers, with the date you received them", "任何法庭文件，並註明收到日期"),
    ]),
    ("business", "A business or company matter", "公司或商業事務", [
        ("Company number and the names of directors and shareholders", "公司註冊號碼、董事及股東名單"),
        ("Articles of association and any shareholders’ agreement", "公司章程及股東協議"),
        ("The contract or draft you want reviewed", "需要審閱的合約或草稿"),
        ("Correspondence with the other side", "與對方的往來書信"),
    ]),
]


def checklist():
    opts = "".join(
        f'<label class="pick"><input type="radio" name="matter" value="{k}"{" checked" if i == 0 else ""}><span>{L(en, zh)}</span></label>'
        for i, (k, en, zh, _) in enumerate(CHECK)
    )
    lists = "".join(
        f'<ul class="ck-list" data-matter="{k}" data-label="{L(en, zh)}"{"" if i == 0 else " hidden"}>' + "".join(
            f'<li><label><input type="checkbox"><span>{L(a, b)}</span></label></li>' for a, b in items
        ) + "</ul>"
        for i, (k, en, zh, items) in enumerate(CHECK)
    )
    return f'''<section class="sec prepare" id="prepare" aria-labelledby="prep-h">
  <div class="wrap prep-grid">
    <div class="prep-intro">
      {tiles("tiles-sm")}
      <h2 id="prep-h">{L('What to bring to your first meeting', '首次見律師 要帶甚麼')}</h2>
      <p>{L('Choose what it is about. You get a list of the papers that usually help, and you can tick them off as you find them. Documents in Chinese are fine: bring them as they are.', '選擇您的事務類型，就會列出通常需要的文件，找到一份就剔一份。中文文件不用翻譯，直接帶來即可。')}</p>
      <p class="fine">{L('A general guide, not legal advice. Nothing you tick is stored.', '只屬一般指引，並非法律意見。您剔選的項目不會被儲存。')}</p>
    </div>
    <form class="ck" data-check>
      <fieldset><legend>{L('It is about', '事務類型')}</legend><div class="picks">{opts}</div></fieldset>
      <div class="ck-sheet">
        <p class="ck-count" aria-live="polite" data-count></p>
        {lists}
        <p class="ck-always">{L('Always bring: photo ID, and a short note of what you want to achieve.', '必須帶備：附相片身份證明文件，以及寫下您希望達到的結果。')}</p>
        <div class="ck-actions">
          <a class="btn btn-mag" data-ck-wa href="https://wa.me/{WA}" target="_blank" rel="noopener">{L('WhatsApp to book a meeting', 'WhatsApp 預約見面')}</a>
          <button class="btn btn-line" type="button" data-print>{L('Print the list', '列印清單')}</button>
        </div>
      </div>
    </form>
  </div>
</section>'''


def ask_form():
    topics = [L(en, zh) for _, en, zh, _ in CHECK] + [L("Something else", "其他")]
    opts = "".join(f"<option>{t}</option>" for t in topics)
    return f'''<form class="ask" id="ask" data-ask novalidate>
  <h2>{L('Send a question', '發送查詢')}</h2>
  <div class="ask-row">
    <label>{L('Your name', '您的名字')}<input name="name" autocomplete="name" required></label>
    <label>{L('Phone or email', '電話或電郵')}<input name="reach" autocomplete="tel" required></label>
  </div>
  <label>{L('It is about', '事務類型')}<select name="topic">{opts}</select></label>
  <label>{L('What happened, and what you would like to achieve', '發生了甚麼事，以及您希望達到的結果')}<textarea name="msg" rows="5" required></textarea></label>
  <p class="err" data-err hidden role="alert">{L('Please fill in your name, how to reach you and your question.', '請填寫名字、聯絡方法及問題。')}</p>
  <div class="ask-actions">
    <button class="btn btn-navy" type="submit" value="wa">{L('Send by WhatsApp', '用 WhatsApp 發送')}</button>
    <button class="btn btn-line" type="submit" value="mail">{L('Send by email', '用電郵發送')}</button>
  </div>
  <p class="fine">{L('This opens WhatsApp or your email app with your message filled in. Nothing is stored on this website.', '按下後會開啟 WhatsApp 或電郵程式並填好內容，本網站不會儲存任何資料。')}</p>
</form>'''


def visit():
    rows = []
    routes = []
    for key, en, zh in STATIONS:
        r = ROUTES[key]
        rows.append(f'<li><span class="v-min">{r["min"]}<small>{L("min", "分鐘")}</small></span><span>{L(en, zh)}<br><small>{r["dist"]} m {L("on foot", "步行")}</small></span></li>')
        routes.append({"name": key, "min": r["min"], "start": r["start"], "coords": r["coords"]})
    data = {"home": HOME, "mark": PX + "assets/img/mark.svg", "label": L("O Tse &amp; Co.", "謝延豐律師行"), "routes": routes}
    return f'''<section class="sec visit" id="visit" aria-labelledby="visit-h">
  <div class="wrap visit-grid">
    <div class="visit-txt">
      <h2 id="visit-h">{L(f'Oxford Place, {ROUTES["Oxford Road"]["min"]} minutes on foot from Oxford Road station', f'Oxford Place 由 Oxford Road 火車站步行 {ROUTES["Oxford Road"]["min"]} 分鐘')}</h2>
      <p class="addr">{ADDR}</p>
      {open_status()}
      <ul class="walks">{''.join(rows)}</ul>
      <p class="fine">{L('Walking times from OpenStreetMap routes. Phone and video meetings for clients anywhere in the UK.', '步行時間按 OpenStreetMap 路線計算。全英國的客戶都可以用電話或視像會面。')}</p>
      <p><a class="btn btn-line" href="https://maps.app.goo.gl/LQid4jvixBQ4nFDKA" target="_blank" rel="noopener">{L('Open in Google Maps', '在 Google 地圖開啟')}</a></p>
    </div>
    <div class="map" data-map data-src="{PX}assets/vendor/maplibre/maplibre-gl.js" data-css="{PX}assets/vendor/maplibre/maplibre-gl.css" data-mapjs="{PX}assets/map.js?v={V}">
      <div class="map-sketch" aria-hidden="true">
        <span class="ms-road ms-ox">Oxford Street</span><span class="ms-road ms-wh">Whitworth Street</span>
        <span class="ms-pin">{mark("ms-mark")}</span>
      </div>
      <script type="application/json" id="map-data">{json.dumps(data, ensure_ascii=False)}</script>
    </div>
  </div>
</section>'''


# ------------------------------------------------------------------ pages
def p_index():
    mag = f'''    <div class="t-mag" lang="zh-Hant-HK">
      <{L('p', 'h1 id="hero-h"')} class="hero-zh"><span>在英國重新起步</span><span>法律上的事</span><span>用廣東話講清楚</span></{L('p', 'h1')}>
      <p class="hero-sub-zh">謝延豐律師行 · 曼徹斯特</p>
    </div>
'''
    nav = f'''    <div class="t-navy" lang="en-GB">
      <{L('h1 id="hero-h"', 'p')} class="hero-en">A Manchester law firm for Hong Kong families starting again</{L('h1', 'p')}>
      <p class="hero-sub-en">O Tse &amp; Co. · Solicitors</p>
    </div>
'''
    TILES = mag + nav if LANG == 'zh' else nav + mag
    hero = f'''<section class="hero" aria-labelledby="hero-h">
  <div class="hero-grid">
{TILES}    <div class="t-side">
      <p class="hero-motto">{L('We listen. We solve legal problems.', '盡心聆聽，解決您的法律問題。')}</p>
      <p>{L('A Manchester law firm regulated by the Solicitors Regulation Authority, serving clients across the UK, in English and Cantonese.', '受英國律師監管局規管的曼徹斯特律師行，以廣東話及英文服務全英國客戶。')}</p>
      <div class="hero-links"><a href="personal.html">{L('For you and your family', '個人及家庭')}</a><a href="business.html">{L('For your business', '公司及生意')}</a></div>
    </div>
    <div class="t-corner">
      <a class="corner-call" href="tel:{TEL}"><small>{L('Call the office', '致電辦公室')}</small>{PHONE}</a>
      <a class="corner-wa" href="{wa(L('Hello, I would like to book a first consultation.', '你好，我想預約首次諮詢。'))}" data-wa><small>WhatsApp</small>{WA_SHOW}</a>
    </div>
    <div class="t-under">
      {open_status()}
      <p>{L('Oxford Place, 61 Oxford Street, Manchester', 'Oxford Place, 61 Oxford Street, Manchester')}</p>
    </div>
  </div>
</section>'''
    doors = f'''<section class="sec doors" aria-labelledby="doors-h">
  <div class="wrap">
    <h2 id="doors-h" class="vh">{L('What we do', '服務範疇')}</h2>
    <div class="door-grid">
      <a class="door door-mag" href="personal.html">
        <span class="door-k">{L('For you and your family', '個人及家庭')}</span>
        <span class="door-h">{L('Buying a home, a will, a tenancy, a problem at work', '買樓、遺囑、租務、工作上的問題')}</span>
        <span class="door-list">{L('Conveyancing · Wills and probate · Family · Employment · Landlord and tenant · Disputes · Defamation · Nuisance', '樓宇買賣 · 遺囑及遺產 · 家庭法 · 勞工法 · 租務糾紛 · 訴訟 · 誹謗 · 滋擾')}</span>
        <span class="door-go">{L('Personal services', '個人服務')} →</span>
      </a>
      <a class="door door-navy" href="business.html">
        <span class="door-k">{L('For your business', '公司及生意')}</span>
        <span class="door-h">{L('Contracts, companies, staff and disputes', '合約、公司、員工及爭議')}</span>
        <span class="door-list">{L('Commercial · Corporate · Employment · Commercial leases · Business disputes', '商業法 · 公司法 · 僱主勞工法 · 商業租務 · 商業爭議')}</span>
        <span class="door-go">{L('Business services', '商業服務')} →</span>
      </a>
    </div>
  </div>
</section>'''
    letter = f'''<section class="sec letter" aria-labelledby="letter-h">
  <div class="wrap letter-grid">
    {tiles("tiles-lg")}
    <div>
      <h2 id="letter-h">{L('“You’re not just clients to us”', '「您在我們心中不僅是客戶」')}</h2>
      <p class="letter-p">{L('We understand that moving to a new country, especially in times like these, can be daunting. That’s why we’re here: to offer a helping hand and a friendly face as you settle into your new home in the UK.', '我們明白移居到新的國家，特別是在這樣的時刻，可能會感到不安。我們願意伸出援手，作為您在英國安居樂業的幫助和依靠。')}</p>
      <p class="letter-sign">{L('O, founder', 'O，創辦人')}</p>
      <p><a class="more" href="about.html">{L('Read the whole letter', '閱讀全文')} →</a></p>
    </div>
  </div>
</section>'''
    cases = f'''<section class="sec cases-sec" aria-labelledby="cases-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="cases-h">{L('Recent cases', '近期案例')}</h2><a class="more" href="cases.html">{L('All cases', '全部案例')} →</a></div>
    {case_cards()}
  </div>
</section>'''
    contact = f'''<section class="sec contact-sec" aria-labelledby="ask-h2">
  <div class="wrap contact-grid">
    <div>
      <h2 id="ask-h2">{L('Tell us what happened', '告訴我們發生了甚麼事')}</h2>
      <p>{L('A short message is enough to start. We reply on working days, in Cantonese or English.', '簡單幾句已經足夠。我們會在工作日以廣東話或英文回覆。')}</p>
      <ul class="ways">
        <li><a href="tel:{TEL}"><small>{L('Office', '辦公室')}</small>{PHONE}</a></li>
        <li><a href="https://wa.me/{WA}" data-wa><small>WhatsApp</small>{WA_SHOW}</a></li>
        <li><a href="mailto:{EMAIL}"><small>{L('Email', '電郵')}</small>{EMAIL}</a></li>
      </ul>
    </div>
    {ask_form()}
  </div>
</section>'''
    body = hero + doors + checklist() + letter + cases + quotes(["tam", "lee"], "mag") + contact + visit()
    return page("index.html", L("O Tse &amp; Co. Solicitors, Manchester (concept)", "謝延豐律師行 曼徹斯特（概念設計）"),
                L("Cantonese-speaking solicitors in Manchester for conveyancing, wills, family, employment and business law.", "曼徹斯特廣東話律師行：樓宇買賣、遺囑、家庭法、勞工法及商業法。"), body)


def p_services(kind):
    personal = kind == "personal"
    tone = "mag" if personal else "navy"
    slug = f"{kind}.html"
    title = L("For you and your family", "個人及家庭") if personal else L("For your business", "公司及生意")
    lead = L("We take pride in giving each client individual legal support, and approach every case with a positive attitude.", "我們以為每位客戶提供專業而個人化的法律支援為榮，並以積極的態度處理每個案件。") if personal else \
        L("Diligent, attentive legal work for businesses of all sizes, with practical solutions that protect your interests.", "為不同規模的企業提供勤勉細心的法律服務，以實際可行的方案保障您的利益。")
    hero = f'''<section class="page-hero ph-{tone}">
  <div class="wrap ph-in">
    <h1>{title}</h1>
    <p>{lead}</p>
  </div>
  {tiles("ph-tiles")}
</section>'''
    areas = f'''<section class="sec" aria-labelledby="areas-h">
  <div class="wrap">
    <h2 id="areas-h">{L('Areas of law', '法律範疇')}</h2>
    {area_list(PERSONAL if personal else BUSINESS, tone)}
  </div>
</section>'''
    if personal:
        deep = [
            ("Conveyancing and land law", "樓宇買賣及土地法",
             "Whether you are a first-time buyer or a seasoned investor, we manage the contractual, regulatory and legal side of the transaction so your investment and property rights are protected. For buyers who moved from Hong Kong, we explain each step, from searches to exchange and completion, in Cantonese.",
             "無論您是首次置業還是有經驗的投資者，我們都會處理交易中的合約、監管及法律事宜，保障您的投資和物業權益。對從香港移居的買家，我們會用廣東話解釋由查冊、交換合約到成交的每一步。"),
            ("Wills and probate", "遺囑及遺產認證",
             "Drafting clear, valid wills, administering estates and navigating probate with sensitivity, including estate litigation, trusts and inheritance disputes. Assets in both the UK and Hong Kong can be planned for together.",
             "起草清晰有效的遺囑，細心處理遺產管理及遺產認證程序，亦處理遺產訴訟、信託及繼承糾紛。英國及香港兩地的資產可以一併規劃。"),
            ("Family law", "家庭法",
             "Divorce, child arrangements, maintenance and property settlements. We aim to resolve disputes amicably, protect your rights firmly when court is necessary, and keep the children’s interests first.",
             "離婚、子女安排、贍養費及財產分配。我們力求以和解方式解決爭議，在必須上庭時堅決保障您的權利，並以子女的最佳利益為先。"),
        ]
    else:
        deep = [
            ("Commercial law", "商業法",
             "Contract negotiation, corporate governance and regulatory compliance, and support with transactions and complex company operations.",
             "合約談判、公司管治及法規遵從，並協助處理商業交易及複雜的公司運作。"),
            ("Business disputes", "商業爭議",
             "Litigation and alternative dispute resolution that protect your interests efficiently and preserve business relationships where possible.",
             "以訴訟及另類排解程序有效保障您的利益，並盡可能維繫商業關係。"),
            ("Employment law for employers", "僱主勞工法",
             "From employment contracts to complex staff issues: we keep you compliant with employment law and defend you in disputes.",
             "由起草僱傭合約到處理複雜的員工關係問題，確保您遵守勞工法，並在爭議中為您辯護。"),
        ]
    deep_html = "".join(
        f'<div class="deep-row"><h3>{L(a, b)}</h3><p>{L(c, d)}</p></div>' for a, b, c, d in deep
    )
    deep_sec = f'''<section class="sec deep deep-{tone}" aria-labelledby="deep-h">
  <div class="wrap">
    <h2 id="deep-h">{L('Where we do most of our work', '我們最有經驗的範疇')}</h2>
    <div class="deep-rows">{deep_html}</div>
  </div>
</section>'''
    cta = f'''<section class="sec cta-band cta-{tone}">
  <div class="wrap cta-in">
    <h2>{L('Not sure which of these it is?', '不肯定屬於哪一類？')}</h2>
    <p>{L('Describe it in a WhatsApp message, in Cantonese or English. We will tell you whether we can help.', '用 WhatsApp 以廣東話或英文簡單說明，我們會告訴您能否協助。')}</p>
    <a class="btn btn-white" href="{wa(L('Hello, I would like to ask about a legal matter.', '你好，我想查詢一件法律事宜。'))}" data-wa>WhatsApp {WA_SHOW}</a>
  </div>
</section>'''
    q = ["tam", "lee", "chan"] if personal else ["chu", "chen", "wong"]
    body = hero + areas + deep_sec + quotes(q, tone) + faq() + cta
    return page(slug, L(f"{title} | O Tse &amp; Co. (concept)", f"{title} | 謝延豐律師行（概念設計）"), lead, body)


def p_cases():
    arts = []
    for k, en_t, zh_t, en_d, zh_d, en_h, zh_h, en_p, zh_p in CASES:
        paras = "".join(f"<p>{x}</p>" for x in L(en_p, zh_p))
        steps = [L("The problem", "問題"), L("What we did", "我們的工作"), L("The outcome", "結果")]
        rows = "".join(f'<div class="cs-step"><h3>{s}</h3>{"<p>" + t + "</p>"}</div>' for s, t in zip(steps, L(en_p, zh_p)))
        arts.append(f'''<article class="case" id="{k}">
  <header><p class="case-meta"><span>{L(en_t, zh_t)}</span> <time>{L(en_d, zh_d)}</time></p><h2>{L(en_h, zh_h)}</h2></header>
  <div class="cs-steps">{rows}</div>
</article>''')
    body = f'''<section class="page-hero ph-paper">
  <div class="wrap ph-in">
    <h1>{L('Cases', '成功案例')}</h1>
    <p>{L('Three recent matters, written up with the client’s details removed. Each one in three parts: the problem, what we did and the outcome.', '三宗近期個案，已刪去客戶個人資料。每宗分為三部分：問題、我們的工作、結果。')}</p>
  </div>
  {tiles("ph-tiles")}
</section>
<section class="sec">
  <div class="wrap cases-list">{''.join(arts)}</div>
</section>
<p class="wrap fine">{L('Past results do not guarantee the outcome of any future case.', '過往結果並不保證日後任何案件的結果。')}</p>'''
    return page("cases.html", L("Cases | O Tse &amp; Co. (concept)", "成功案例 | 謝延豐律師行（概念設計）"),
                L("Recent employment, conveyancing and probate cases.", "勞工法、樓宇買賣及遺產認證的近期個案。"), body)


def p_about():
    letter_en = [
        "Hello everyone,",
        "Welcome to O Tse &amp; Co. Limited! I’m O, and I’m absolutely delighted to have you with us. As we embark on this journey together, I want you to know that you’re not just clients to us; you’re part of our extended family.",
        "We understand that moving to a new country, especially in times like these, can be daunting. That’s why we’re here: to offer a helping hand and a friendly face as you settle into your new home in the UK. Whether it’s navigating legal matters or simply finding your feet in a new community, we’re here to support you every step of the way.",
        "At O Tse &amp; Co. Limited, we’re all about creating meaningful connections and providing personalised care. So please, don’t hesitate to reach out whenever you need assistance or just want to chat.",
        "Warmest regards,",
    ]
    letter_zh = [
        "大家好，",
        "歡迎各位來到 O Tse &amp; Co. Limited！非常高興能夠與大家在這裡相聚。當我們攜手展開這段旅程時，您在我們心中不僅是客戶，更是我們家庭的一份子。",
        "我們明白移居到新的國家，特別是在這樣的時刻，可能會感到不安。我們願意伸出援手，作為您在英國安居樂業的幫助和依靠。無論是處理法律事務，還是在新的社區安家落戶，我們都會全力支持您。",
        "在 O Tse &amp; Co. Limited，我們重視與客戶之間建立真誠的聯繫，並提供度身訂造的服務。請隨時與我們聯繫，無論是需要法律上的幫助還是只是想聊聊天。",
        "此致",
    ]
    vals = [
        ("Every area under one roof", "一站式法律服務",
         "Conveyancing, corporate matters, employment and personal disputes: one firm for the legal side of a new life.",
         "樓宇買賣、公司事務、勞工法及個人糾紛：新生活的法律事務，一間律師行處理。"),
        ("Regular, plain updates", "定期而清楚的進度匯報",
         "We keep you informed throughout, answer questions promptly and tell you plainly where your case stands.",
         "我們會持續更新案件進展，及時解答疑問，清楚告訴您案件的狀況。"),
        ("Your goals first", "以客戶為先",
         "From the first consultation to the end of the matter, we work from your circumstances, concerns and goals.",
         "由首次諮詢到事情完結，我們都會從您的情況、顧慮和目標出發。"),
    ]
    vals_html = "".join(f'<li><h3>{L(a, b)}</h3><p>{L(c, d)}</p></li>' for a, b, c, d in vals)
    body = f'''<section class="page-hero ph-navy">
  <div class="wrap ph-in">
    <h1>{L('Based in Manchester, working nationwide', '扎根曼徹斯特 服務全英國')}</h1>
    <p>{L('As Hong Kong’s diaspora finds its footing in the United Kingdom, we offer legal help tailored to people starting anew: advice, and also empathy and support. Fluent in Cantonese, so everyone feels understood.', '隨著越來越多香港人移居英國開展新生活，我們為重新起步的您提供全面的法律協助：不只是法律意見，還有理解和支持。我們精通廣東話，確保明白您的需要。')}</p>
  </div>
  {tiles("ph-tiles")}
</section>
<section class="sec">
  <div class="wrap about-grid">
    <article class="letter-full" aria-labelledby="lt-h">
      <h2 id="lt-h">{L('A letter from the founder', '創辦人的信')}</h2>
      {''.join('<p>' + x + '</p>' for x in L(letter_en, letter_zh))}
      <p class="letter-sign">{L('O, founder of O Tse &amp; Co. Limited', 'O Tse &amp; Co. Limited 創辦人 O')}</p>
    </article>
    <aside class="facts">
      {mark("facts-mark")}
      <dl>
        <dt>{L('Firm', '律師行')}</dt><dd>O Tse &amp; Co. Limited<br><span lang="zh-Hant">謝延豐律師行</span></dd>
        <dt>{L('Regulator', '監管機構')}</dt><dd>{L('Solicitors Regulation Authority, authorised for all legal services', '英國律師監管局，獲授權提供所有法律服務')}</dd>
        <dt>{L('Languages', '語言')}</dt><dd>{L('Cantonese and English', '廣東話及英文')}</dd>
        <dt>{L('Office', '辦公室')}</dt><dd>{ADDR}</dd>
      </dl>
    </aside>
  </div>
</section>
<section class="sec vals-sec" aria-labelledby="vals-h">
  <div class="wrap">
    <h2 id="vals-h">{L('Why clients choose us', '客戶選擇我們的原因')}</h2>
    <ul class="vals">{vals_html}</ul>
  </div>
</section>'''
    return page("about.html", L("About | O Tse &amp; Co. (concept)", "關於我們 | 謝延豐律師行（概念設計）"),
                L("A Manchester law firm for the Hong Kong community in the UK.", "服務在英香港人的曼徹斯特律師行。"), body)


def p_contact():
    body = f'''<section class="page-hero ph-paper">
  <div class="wrap ph-in">
    <h1>{L('Contact', '聯絡我們')}</h1>
    <p>{L('Call, WhatsApp or email. Meetings at the office on Oxford Street, or by phone and video anywhere in the UK.', '致電、WhatsApp 或電郵。可到 Oxford Street 辦公室見面，亦可以電話或視像進行，服務全英國。')}</p>
  </div>
  {tiles("ph-tiles")}
</section>
<section class="sec">
  <div class="wrap contact-grid">
    <div>
      <ul class="ways ways-big">
        <li><a href="tel:{TEL}"><small>{L('Office', '辦公室')}</small>{PHONE}</a></li>
        <li><a href="https://wa.me/{WA}" data-wa><small>WhatsApp</small>{WA_SHOW}</a></li>
        <li><a href="mailto:{EMAIL}"><small>{L('Email', '電郵')}</small>{EMAIL}</a></li>
      </ul>
      {open_status()}
      <p class="fine">{L('Closed at weekends and on public holidays.', '週末及公眾假期休息。')}</p>
    </div>
    {ask_form()}
  </div>
</section>
{checklist()}
{visit()}'''
    return page("contact.html", L("Contact | O Tse &amp; Co. (concept)", "聯絡我們 | 謝延豐律師行（概念設計）"),
                L("Phone, WhatsApp, email and directions to Oxford Place, Manchester.", "電話、WhatsApp、電郵及前往 Oxford Place 的路線。"), body)


def p_privacy():
    en = f'''<h2>Privacy notice</h2>
<p><strong>Draft for O Tse &amp; Co. to review.</strong> The current website links to a privacy policy but the link goes nowhere, so this concept includes a starting point.</p>
<h3>Who we are</h3><p>O Tse &amp; Co. Limited, {ADDR}, is the controller of personal data you give us. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h3>What we collect and why</h3><p>When you contact us we use your name, contact details and what you tell us about your matter to reply and, if you instruct us, to act for you. If you become a client we also hold identity documents to meet anti-money-laundering rules, and records of your matter as our regulator requires.</p>
<h3>How long we keep it</h3><p>Enquiries that do not become instructions are deleted after a reasonable period. Client files are kept for the period required by law and professional rules, usually at least six years after the matter ends.</p>
<h3>Your rights</h3><p>You can ask for a copy of your data, ask us to correct or delete it, or object to how we use it. You can complain to the Information Commissioner’s Office at ico.org.uk.</p>
<h3>This website</h3><p>This concept site sets no cookies and stores nothing. The contact form opens WhatsApp or your email app; the message is only sent if you send it there. The map loads tiles from OpenFreeMap when you scroll to it.</p>
<h2>Accessibility</h2>
<p>This site aims to meet WCAG 2.2 AA: text contrast, keyboard navigation with visible focus, a skip link, real headings, and respect for reduced-motion settings. If something does not work for you, call <a href="tel:{TEL}">{PHONE}</a> and we will help by phone.</p>'''
    zh = f'''<h2>私隱聲明</h2>
<p><strong>草稿，需由謝延豐律師行審閱。</strong>現有網站有「私隱政策」的字眼但沒有連結，因此概念設計提供一個起點。</p>
<h3>我們是誰</h3><p>O Tse &amp; Co. Limited（{ADDR}）是您提供的個人資料的控制者。聯絡：<a href="mailto:{EMAIL}">{EMAIL}</a>。</p>
<h3>收集甚麼資料及用途</h3><p>您聯絡我們時，我們會使用您的名字、聯絡方法及您提供的事件資料作回覆；如您委託我們，則用於代表您處理事務。成為客戶後，我們亦須按反洗錢規定保存身份證明文件，並按監管要求保存案件紀錄。</p>
<h3>保存期限</h3><p>沒有成為委託的查詢會在合理期間後刪除。客戶檔案按法律及專業守則要求保存，一般為事務完結後最少六年。</p>
<h3>您的權利</h3><p>您可以要求取得資料副本、更正或刪除資料，或反對我們使用資料的方式，亦可向資訊專員辦公室（ico.org.uk）投訴。</p>
<h3>本網站</h3><p>本概念網站不設 cookies，亦不儲存任何資料。聯絡表格只會開啟 WhatsApp 或電郵程式，由您決定是否發送。地圖在您捲動到該處時才從 OpenFreeMap 載入。</p>
<h2>無障礙</h2>
<p>本網站以符合 WCAG 2.2 AA 為目標：文字對比、可用鍵盤操作並有清晰焦點、跳至內容連結、正確標題結構，以及尊重減少動態效果的設定。如有任何地方無法使用，請致電 <a href="tel:{TEL}">{PHONE}</a>，我們會在電話上協助您。</p>'''
    body = f'''<section class="page-hero ph-paper"><div class="wrap ph-in"><h1>{L('Privacy and accessibility', '私隱及無障礙')}</h1></div>{tiles("ph-tiles")}</section>
<section class="sec"><div class="wrap prose">{L(en, zh)}</div></section>'''
    return page("privacy.html", L("Privacy and accessibility | O Tse &amp; Co. (concept)", "私隱及無障礙 | 謝延豐律師行（概念設計）"),
                L("Privacy notice and accessibility statement.", "私隱聲明及無障礙聲明。"), body)


def p_404():
    body = f'''<section class="lost">
  <div class="wrap lost-in">
    <div class="tiles tiles-apart" aria-hidden="true"><i></i><i></i></div>
    <h1>{L('This page doesn’t meet up with anything', '這一頁對不上任何內容')}</h1>
    <p>{L('The link may be old or mistyped.', '連結可能已過時或輸入有誤。')}</p>
    <p><a class="btn btn-navy" href="{PX}{L('', 'zh/')}index.html">{L('Back to the home page', '返回主頁')}</a></p>
  </div>
</section>'''
    return page("404.html", L("Page not found | O Tse &amp; Co. (concept)", "找不到頁面 | 謝延豐律師行（概念設計）"), "", body)


def build():
    global LANG, PX
    for lang, sub in (("en", ""), ("zh", "zh/")):
        LANG = lang
        PX = "" if lang == "en" else "../"
        out = os.path.join(ROOT, sub)
        os.makedirs(out, exist_ok=True)
        pages = {
            "index.html": p_index(), "personal.html": p_services("personal"), "business.html": p_services("business"),
            "cases.html": p_cases(), "about.html": p_about(), "contact.html": p_contact(), "privacy.html": p_privacy(),
        }
        for name, html in pages.items():
            open(os.path.join(out, name), "w", encoding="utf-8").write(html)
    # 404 at root uses absolute links so it works from any depth
    LANG, PX = "en", BASE
    html = p_404().replace('href="index.html"', f'href="{BASE}"')
    for h, _, _ in NAV:
        html = html.replace(f'href="{h}"', f'href="{BASE}{h}"')
    html = html.replace('href="privacy.html"', f'href="{BASE}privacy.html"').replace('href="#ask"', f'href="{BASE}contact.html#ask"').replace('href="contact.html#ask"', f'href="{BASE}contact.html#ask"')
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(html)
    print("built")


if __name__ == "__main__":
    build()
