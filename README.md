## 題目：Restaurant Booking Platform
### 問題描述：
實作餐廳訂位系統，並根據顧客回饋做出餐廳推薦，增加使用者使用的意願。
### 資料結構：Heap、List、Dictionary
### 主要功能：
#### ● 訂位：
使用者輸入訂位的姓名、星期、時間，介面會列出所有餐廳剩下的座位數還有依
據顧客給的評價做出的推薦，依據設定可以是Top-K推薦。顧客依據推薦和座位
剩下的數量來決定要訂哪家餐廳。
#### ● 取消訂位：
使用者輸入姓名、星期和時間，系統便會取消訂位，並顯示取消成功。
#### ● 修改訂位：
使用者輸入姓名、星期、時間和餐廳，系統便會列出已訂位人數，此時顧客可以
減少訂位人數，並顯示修改成功。
#### ● 查看訂位情況：
使用者輸入姓名、星期和時間，系統會顯示該顧客歷史訂位資料。
#### ● 留下評價：
使用者在用餐完畢後，可以選擇進入系統對餐廳進行評價(1-5分)，然後系統會自
動更新資料庫，將顧客的評分加總後取平均然後更新，做為下次有人訂位時，系
統推薦餐廳的依據。
### 動機：
疫情當道，希望在外面用餐時能降低群聚機會，想建立一個訂位平台，方便人們預約餐
廳，同時可知道各餐廳剩下的座位，讓顧客能根據空位率和平台推薦，來最佳化餐廳的
選擇。
### 技術挑戰性：
#### ● 資料結構：
使用資料結構實現餐廳評價推薦的時候，因為顧客會不斷進入平台系
統評分，需要對該餐廳的評價進行更新，所以無法直接使用第五次作業取Top-K
的演算法。
#### ● GUI: 
需熟悉tkinter package 的各式函數，並利用按鈕取代人機互動，來呼叫或
更新資料庫，因此容易出現bug，所以花了不少時間debug。
### 時間複雜度：O(N logK)
第五個功能留下評價，使用了Top-K的演算法。每次新的顧客留下評價，便會更新該餐廳
的評價分數，並重新排序取出前K高評價的餐廳。
有兩種實現方式：
1. Sorting：用sorting直接把N家餐廳做排序然後取前K個，時間複雜度是 O(N
logN)。
2. Heap：建立一個Heap，跑迴圈未滿K個餐廳時依序將餐廳放入，直到K個餐廳之
後，每放入一個餐廳之前先比較Heap中評價最低的餐廳和新的餐廳，若新的餐
廳評價較高，則取代原先的餐廳並進行Heap的調整；反之則不改動Heap並進行
下一個餐廳的判斷。Heap調整的時間複雜度O(logK)，因為要進行N次如此的動
作，時間複雜度是O(N logK)。最後，還要將這K家餐廳進行排序，但在N>>K的情
況，時間複雜度並不受影響，還是O(N logK)。
### 執行方式：用main file中的檔案來執行
