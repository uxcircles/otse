# O Tse & Co.（謝延豐律師行）概念網站

UX CIRCLES 為曼徹斯特 O Tse & Co. Limited 製作的**非官方改版概念**。官方網站：https://otse.co.uk/
每頁頂部有「概念」橫條，所有頁面 `noindex, nofollow`，`robots.txt` 禁止搜尋引擎收錄。

網址（發佈後）：https://uxcircles.github.io/otse/ ・ 中文：https://uxcircles.github.io/otse/zh/

## 頁面

| 英文 | 中文 | 內容 |
|---|---|---|
| `index.html` | `zh/index.html` | 首頁：雙語方塊 hero、個人／商業服務、首次見面清單、創辦人的話、案例、聯絡表格、地圖 |
| `personal.html` | `zh/personal.html` | 個人服務（8 個範疇）、客戶評語、常見問題 |
| `business.html` | `zh/business.html` | 商業服務（5 個範疇） |
| `cases.html` | `zh/cases.html` | 3 宗案例，分「問題／我們的工作／結果」 |
| `about.html` | `zh/about.html` | 創辦人的信、律師行資料 |
| `contact.html` | `zh/contact.html` | 聯絡方法、表格、清單工具、步行路線地圖 |
| `privacy.html` | `zh/privacy.html` | 私隱聲明及無障礙聲明（草稿） |
| `404.html` | | 找不到頁面 |

## 如何修改

所有頁面由 `_build/pages.py` 產生，文字以 `L(英文, 中文)` 並排寫在一起：

```bash
python3 _build/pages.py && python3 _build/fonts.py   # 改了中文字之後要重跑 fonts.py
```

改 CSS/JS 後把 `pages.py` 裡的 `V` 加一（cache-bust）。地圖顏色在 `assets/map.js` 頂部的 `C`。
步行路線（routing.openstreetmap.de）存在 `_build/routes.json`。

## 設計概念

- **標誌元素**：律師行標誌的兩塊方塊：洋紅方塊（左上圓角）和深藍方塊（右下圓角）在一個角相接。概念：香港與曼城在一個角上相遇。
- **Hero（bilingual-split）**：首屏就是放大的標誌：洋紅方塊寫中文標題，深藍方塊寫英文標題，電話和 WhatsApp 放在兩塊相接的角落。手機版以該頁語言的方塊在前。
- **延伸**：個人服務＝洋紅，商業服務＝深藍；分隔用的小方塊、頁首方塊、地圖 pin、favicon、頁尾，以及 404（兩塊方塊對不上）。
- **字體**：Familjen Grotesk（英文標題）、Onest（英文內文）、Chiron Sung HK（中文標題，香港字形）、Noto Sans TC（中文內文）。全部自行託管，中文只保留網站用到的字。
- **顏色**：#9b2358 洋紅、#2a3b6f 深藍，直接取自標誌 SVG；底色 #f3f2ef。
- **標題**：英文「A Manchester law firm for Hong Kong families starting again」（取自 About 頁 "we warmly welcome those starting anew"）；中文「在英國重新起步 法律上的事 用廣東話講清楚」。
- **工具**：「首次見律師要帶甚麼」清單：按事務類型列出文件，可剔選、列印，或用 WhatsApp 預約。不儲存任何資料，標明只屬一般指引。
- **與之前律師行概念的分別**：Chung & Rea 是文件物件 hero、Young Serif、淺色；Lu Oliphant／Lee & Kan 是左文右卡片。這次不用相片、不用卡片，是第一個 bilingual-split；第一次用洋紅作主色。
- 相似度檢查提示「大圓角」：那是標誌本身的單一圓角（只圓一角），不是拱形相框，因此保留。

## 需要律師行確認的資料

- **SRA 編號及數碼徽章**：現有網站只寫「受 SRA 規管」，沒有編號，亦沒有 SRA 要求展示的數碼徽章（digital badge）。本概念未填寫，需律師行提供。
- **收費資料**：SRA Transparency Rules 要求就住宅樓宇買賣、遺產認證及勞資審裁處申索等服務公佈收費資料，現有網站只寫「費用視乎情況」。本概念未加入收費，需律師行提供。
- **辦公時間**：大部分頁面寫星期一至五，但英文 Personal 頁寫「Monday - Saturday」。本概念用星期一至五。
- **客戶評語及案例**：照搬現有網站已公開的內容，沒有新增。
- **私隱聲明**：現有網站的 Privacy Policy、FAQ、Site Map、Cookie Policy 都沒有實際連結；本概念的私隱聲明是草稿，需律師行審閱。
- 沒有使用相片（沒有圖庫人物冒充員工）。
- 公司註冊資料：Companies House 上 O TSE & CO. LIMITED 的編號為 14370444（2022 年 9 月 22 日成立），本概念未顯示，請確認後可加入頁尾。
