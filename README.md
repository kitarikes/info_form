<h2 align="center"> :postbox: お問い合わせフォーム</h2>
webアプリの練習として、簡単なお問い合わせフォームを作りました。<br>

![info_mv](https://user-images.githubusercontent.com/52794486/78278951-c409d180-7551-11ea-8588-4d645faf1216.gif)

### :sparkles: 機能:
- データの送信
- 送信直前の確認ページ
- jqueryでの入力形式チェック and 警告
- お問い合わせで受信したデータの表示と削除

<h3 align="center">使用技術</h3>
<p align="center">
  <a href="[flask公式サイトURL](https://a2c.bitbucket.io/flask/)"><img src="https://a2c.bitbucket.io/flask/_images/logo-full.png" height="45px;" /></a><br>
  <a href="[jquery公式サイトURL](https://jquery.com/)"><img src="https://syncer.jp/storage/web/brand-logos/static/dst/jquery-logo-001.png" height="45px;" /></a>
  <a href="[bootstrap公式サイトURL](https://getbootstrap.com/)"><img src="https://www.yutaliberty.com/wp-content/uploads/2019/03/bootstrap-logo.png" height="45px;" /></a>
  <a href="[heroku公式サイトURL](https://jp.heroku.com/)"><img src="https://cdn-ak.f.st-hatena.com/images/fotolife/y/yazawa_tech/20190705/20190705103445.png" height="45px;" /></a>

</p>

## 🌐 App URL

### **https://kita-info-app.herokuapp.com/info**  
　
## :paperclip: 参考にしたサイト

### flask
- [Flask + SQLAlchemyプロジェクトを始める手順](https://qiita.com/shirakiya/items/0114d51e9c189658002e)
- [VS CodeとFlask-SQLAlchemyでデータベース操作 (2/2)](https://www.atmarkit.co.jp/ait/articles/1808/07/news029_2.html)
- [sqlalchemyチュートリアル](https://qiita.com/msrks/items/15144746ff4f7aced4b5)
- [MySQLコマンドまとめ](https://qiita.com/merrill/items/967884c02e10bd8f32f5#%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E6%93%8D%E4%BD%9C)

### UI
- [とほほのBootstrap 4入門 テキスト・パスワード・テキストボックス](http://www.tohoho-web.com/bootstrap/forms.html)
- [Bootstrap 4でブロック中央寄せ](https://qiita.com/Fendo181/items/1f32cbbfa676766ae331)
- [Bootstrapでテーブルを利用する方法](https://qiita.com/AquaMeria/items/b94d1d9ba074f04336b9#%E3%83%AC%E3%82%B9%E3%83%9D%E3%83%B3%E3%82%B7%E3%83%96)

## :warning: デプロイ時のエラーや注意

```Console
$ heroku run FLASK_APP=run.py flask shell
 »   Warning: heroku update available from 7.29.0 to 7.39.1.
Running FLASK_APP=run.py flask shell on ⬢ kita-info-app... up, run.7510 (Free)
Python 3.7.3 (default, Apr  3 2019, 21:35:17) 
[GCC 7.3.0] on linux
App: flask_sample.app [production]
Instance: /app/instance
>>> from flask_sample.database import db
>>> db.create_all()

これでテーブルが生成される
```
※pip freeze で`psycopg2`を忘れないようにする

dynoの同時起動エラー

```Console
>> heroku ps:stop run.7454 --app q-zaka
```
で解消。