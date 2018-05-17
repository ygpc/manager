// phina.js をグローバル領域に展開
phina.globalize();

var ASSETS={
	image: {
		'background':'sae4.gif',
	},
};

// MainScene クラスを定義
phina.define('MainScene', {
  superClass: 'CanvasScene',
  init: function() {
    this.superInit();
    // 背景色を指定
    //this.backgroundColor = '#444';
    // ラベルを生成
    //this.label = Label('Hello, phina.js!').addChildTo(this);
    //this.label.x = this.gridX.center(); // x 座標
    //this.label.y = this.gridY.center(); // y 座標
    //this.label.fill = 'white'; // 塗りつぶし色
		var sprite=Sprite('background').addChildTo(this);

		sprite.x=this.gridX.center();
		sprite.y=this.gridY.center();

		sprite.update =function(){
			sprite.scaleX=1.3;
			sprite.scaleY=1.3;
		};
		//var shape = RectangleShape().addChildTo(this);
		//shape.setPosition(320,480);
		var label=Label("text").addChildTo(this);
		label.setPosition(320,850);
		label.backgroundColor='#444';
  },
});

// メイン処理
phina.main(function() {
  // アプリケーション生成
  var app = GameApp({
    startLabel: 'main', // メインシーンから開始する
		assets: ASSETS,
  });
  // アプリケーション実行
  app.run();
});
