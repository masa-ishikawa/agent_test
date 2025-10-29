# 本ハンズオンについて

- **内容**
OCI Generative AI ServiceとAgent Development Kitを利用したAIエージェントの実装について基本的な手順を学習します。

- **時間**
約60分

- **ハンズオン環境**
下記の環境を構築します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/3b34f799-ad4a-416e-bfa4-768fcccc15f6.png)

**OCI Generative AI Agents Service**
AIエージェントを構築するためのクラウドサービスです。本ハンズオンではウィザード形式のGUI操作でAIエージェントのエンドポイントまでをGUIツールで実施します。このサービスではLLM(Llama3)を包含していますので、別途LLMが必要になることはありません。

**Agent Development Kit(ADK)**
OCI Generative AI Agents ServiceでAIエージェントを構築するためのSDKです。作成されたエンドポイントを使ってAIエージェントの処理を定義するために使用します。こちらはPythonまたはJavaのライブラリとなり、コーディングによる開発となります。

**OCI Data Science Service**
本ハンズオンではADKを使ってPythonで処理を定義するため、Pythonノートブック環境としてOCI Data Science Serviceを利用します。

# Oracle Cloudログイン後、リージョン確認

作成したアカウントでオラクルクラウドにログインすると下記のトップページが表示されます。

まず、右上赤枠のリージョンがGenerative AI Serviceを利用できるリージョンであることを確認してください。
> ⚠️ **注意:**  
> 今回は **Chicago リージョン** を例にしていますが、**Ashburn リージョン** でも利用可能です。  
> どちらを選んでも構いません。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/382d49c4-55fa-4702-884f-24638852545a.png)

左上赤枠がコンソールメニューバーとなり、ここから様々なサービスや設定画面に移動できます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/90efed45-0866-48d3-a23d-f6943f5e31cd.png)

# コンパートメントの作成

コンパートメントを作成します。下記のように辿ってコンパートメント作成画面に移動してください。

**コンソールメニュー　＞　アイデンティティとセキュリティ　＞　コンパートメント　＞　コンパートメントの作成ボタン**

設定項目としては下記の通りです。
- 名前：hol（任意）
- 説明：hol（任意）

その他の項目はデフォルトでコンパートメントの作成ボタンをクリックしてください。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/68fb3ec2-09b7-43a7-b24b-f59285477583.png)







# Python環境の構築(Data Science Service)

作成したコンパートメントにOCI Data Science Service のインスタンスを作成します。
下記のように辿って、プロジェクトを作成画面に移動します。

**コンソールメニュー　＞　アナリティクスとAI　＞　データサイエンス　＞　プロジェクトの作成**

作成済みのコンパートメントであることを確認しプロジェクトの作成ボタンをクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/5f9f4b6c-fe55-4233-97bc-f6042422258b.png)

設定項目は下記の通り。
- コンパートメント：hol
- 名前：hol（任意）

作成ボタンをクリックしプロジェクトを作成します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/7422b25c-ecb5-462e-adf6-cdc4d8a0b78f.png)


作成済のプロジェクトにノートブックセッションを作成します。
ノートブックセッションの作成ボタンをクリックします。


![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/a70de870-e34d-4145-8c5f-5e79b2ddf2df.png)

ノートブック・セッションの作成画面での設定項目は下記の通り。
- コンパートメント：hol
- 名前：hol（任意）

更に、シェイプの変更ボタンをクリックし、シェイプを設定します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/0d5ecbbc-63a4-465f-a7af-991a14d37d8d.png)



今回はVM.Standard.E4.Flexインスタンスを使用します。
下記のリソースを選択します。

- インスタンス・タイプ：仮想マシン
- シェイプシリーズ：AMD

次に、シェイプの選択ボタンをクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/a0a97754-2d9a-40b1-b409-286535693e2d.png)

ここでCPU、メモリのリソース設定を行います。
今回は下記のリソースで十分です。

- OCPU : 2
- メモリー : 16

その他の項目についてはデフォルトで問題ありません。作成ボタンをクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/22c15058-706f-4066-97ce-faeb2c9ec3d2.png)

ノートブック・セッション作成画面に戻り、作成ボタンをクリックします。
(今回ブロックストレージのサイズはデフォルトの100GBで十分なので指定しません。)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/90c4aaa3-184b-40ca-bacd-31bb9c992ed4.png)

作成したノートブック・セッションは数分で起動します。作成したノートブックのリンクをクリックし詳細画面に移動します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/3d52ffef-78ac-467b-be40-7dc77251fe86.png)

ノートブックセッションの「開く」ボタンをクリックしノートブックの画面に移動します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/5d65b101-55d6-4301-9060-4d516680ab1e.png)

下記の画面が表示されればノートブックが利用可能な状態になっています。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/aaf79cf6-7c78-4999-b8f7-fcdc10434f99.png)

# Conda仮想環境の作成

作成したノートブックセッションのPython環境にConda仮想環境を作ってゆきます。
まずはTerminalのアイコンをクリックし、ターミナルを開きます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/9eea1d8f-80a9-440e-8bea-a62d362e4547.png)

ターミナルで下記コマンドを実行し、Conda仮想環境を作成します。

```bash
odsc conda install -s python_p312_any_x86_64_v1 
```

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/38dd5def-b065-458d-9bfb-842a6de110cd.png)

下記コマンドで作成されているconda仮想環境を確認します。

```python
(base) bash-4.4$ conda env list

# conda environments:
#
                       /home/datascience/conda/python_p312_any_x86_64_v1
base                 * /opt/conda
odscruntimeconfig      /opt/conda/envs/odscruntimeconfig
```

下記コマンドで作成済の仮想環境をactivateします。

```python
(base) bash-4.4$ conda activate /home/datascience/conda/python_p312_any_x86_64_v1
(/home/datascience/conda/python_p312_any_x86_64_v1) bash-4.4$ 
```

問題なくactivateできましたら、Conda仮想環境の準備は完了です。

(後の手順でTerminalでの操作を行いますのでData Science Serviceの画面は常に利用できるようにしておいてください。)











# APIキーの登録

APIキーの登録に必要なRSAキー・ペアと認証設定ファイルをOCICLIで作成します。

まず、OCICLIセットアップ時に入力が求められるユーザーOCIDとテナンシOCIDをメモ帳などにコピーしておく作業を行います。

コンソール右上のプロファイルメニューからユーザー名をクリックし、ユーザーの詳細画面に移動します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/b0e2fb2c-4cfb-46a9-9423-12fab2e5a8c0.png)

ユーザーの詳細画面にてOCIDの項目の右側のコピーボタンをクリックし、メモ帳などにペーストします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/1021df15-a4cd-44ec-83cd-bf83622fe166.png)

値としては以下のようなものになっているはずです。こちらがユーザーOCIDです。

```text
ocid1.user.oc1..aaaaaaa<中略>nqjja
```

同じくコンソール右上のプロファイルメニューからテナンシをクリックし、テナンシの詳細画面に移動します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/0b960443-729e-40b7-b19b-f0c458817203.png)

同じく、テナンシの詳細画面にてOCIDの右側にあるコピーボタンをクリックし、メモ帳などにペーストします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/b4ea20d1-9cce-4f00-b09c-ef7ccde42aec.png)

値としては以下のようなものになっているはずです。こちらがテナンシOCIDです。

```text
ocid1.tenancy.oc1..aaaaaaaas<中略>vcmp4qsq
```

次にOCICLIのセットアップです。ターミナルから下記コマンドを実行します。

```bash
oci setup config 
```

💡: 下の画像では初期状態のパスですが、conda仮想環境のアクティブ直後のターミナル上のパスで実行しても問題ありません。


![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/41846de2-5232-4633-9808-7729bf2dd328.png)

コマンドプロンプトで求められる以下の項目を入力します

```bash
# 入力なしでリターン。
Enter a location for your config [/home/datascience/.oci/config]: 

# ご自身のユーザーOCIDを入力しリターン。
Enter a user OCID : ocid1.user.oc1..aaaaaxxxxxxxxxxxx

# ご自身のテナンシOCIDを入力しリターン。
Enter a tenancy OCID:　ocid1.tenancy.oc1..aaaaaaaxxxxxxxxxx

# ご自身の利用リージョンのインデックス値を入力しリターン。
Enter a region by index or name : (表示されるus-chicago-1のindex値)

# RSAキーペアを作成します。「Y」でリターン。
Do you want to generate a new API Signing RSA key pair? (If you decline you will be asked to supply the path to an existing key.) [Y/n]: Y

# 入力なしでリターン。
Enter a directory for your keys to be created [/home/datascience/.oci]:

# 入力なしでリターン。
Enter a name for your key [oci_api_key]:

# パスワードは任意ですが、今回は Welcome1#Welcome1# で設定してください。
Enter a passphrase for your private key ("N/A" for no passphrase): Welcome1#Welcome1#
Repeat for confirmation:
Do you want to write your passphrase to the config file? (If not, you will need to enter it when prompted each time you run an oci command) [y/N]: y
```

上記の入力でRSAキーや認証設定ファイルが ~/.oci ディレクトリに作成されている状態になります。
作成された公開鍵をAPIキーとして登録しますので下記コマンドで鍵を表示してターミナルでコピーしてください。

```bash
(base) bash-4.4$ cat ~/.oci/oci_api_key_public.pem 
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAze4tiewg+rHcTJE/dDdO
(マスク)
Kr8pHLBX391XRRCJfm6KyzifZCF5SzJWGzQ06Zk/2c+Z33bWzKy7/CU+3mK1+bQ6
tQIDAQAB
-----END PUBLIC KEY-----
```

次にコンソール右上のプロファイルからユーザー名をクリックし、ユーザーの詳細画面に移動します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/f4b0d5ef-4423-4b62-b140-4f5b4f41260f.png)


ユーザー詳細画面左のトークンおよびキーをクリックし、APIキーの追加ボタンをクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/54de0f6c-c2db-46d1-9c2b-f26d494374d4.png)

公開キーの貼り付けを選択し、先ほどコピーした公開鍵を公開キーのフィールドにペーストし、追加ボタンをクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/e0b14a2b-bc3f-4a57-a50a-125b845eae2f.png)


下記確認画面で閉じるボタンをクリック。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/e8b2a0ef-e361-49c6-92d8-884ffa8dc57f.png)

APIキーが追加されていることが確認できます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/e3b075c3-2f9a-47b5-8d21-564dcca6fbad.png)

認証ができるかどうかを確認します。
Data Science Serviceの画面に戻り、terminalから下記コマンド(利用できるリージョンのリストを表示)を実行し、結果が表示されることを確認してください。

💡: 設定反映まで5分弱ほどかかりますので少々お待ちだください☕

```bash
(base) bash-4.4$ oci iam region list
{
  "data": [
    {
      "key": "ORD",
      "name": "us-chicago-1"
    },
...
...

```

# OCI Generative AI Agents Serviceでのエージェント・エンドポイントの作成

下記のように辿り、生成AIエージェントサービスのホーム画面に移動します。
**コンソールメニュー　＞　アナリティクスとAI　＞　生成AIエージェント**

生成AIエージェントサービスのホーム画面左の「エージェント」をクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/25108ce3-9685-4ff7-bd2d-d36ea9438472.png)

エージェントの詳細画面にて「エージェント作成」をクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/1c68564d-c47f-4d40-b2cc-8810a96c9dae.png)

エージェントの基本情報を入力します。

- 名前：quickstart(任意)
- コンパートメント：事前に作成したコンパートメントを選択

「次」へ

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/554bb5ad-5520-468e-ab89-1862d2e518b9.png)

ツール画面では何も操作はせず「次」へ
(※後の工程でAgent Development Kitにより定義しますのでGUIでの設定はありません。)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/5846fdea-9ed9-4458-9824-8a41b28fc21d.png)

「このエージェントのエンドポイントの自動作成」にチェックが入っていることを確認し「次」へ
(今回はガードレールなどの設定は行いませんが、実環境では必要に応じて設定してください。)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/60f7ed07-3468-460a-8ff4-ce5c5579e576.png)

作成するエージェントの設定確認画面です。ここまで設定した内容を確認し問題なければ「エージェントの作成」をクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/15d76ae7-1a96-44e3-9d06-5481ac78ec93.png)

本サービスではLLMとしてLlama3を使うことになりますので利用規定に同意し「送信」をクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/158b3471-d0f8-48e8-bb36-b8669c7a6911.png)

エージェントが作成され、アクティブになった後、作成したエージェントをクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/6b102895-c889-492f-b3cf-9605c97a0e6a.png)

エージェントの詳細画面のエンドポイントをクリックします。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/5984f9dd-50ba-47ba-b6fb-f4ec87bf1178.png)

作成されたエージェントのエンドポイントのOCIDの横にある「コピー」をクリックし、メモ帳などに控ええておきます。(このエンドポイントのOCIDは後のPythonコードに利用します。)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/109260/1a1c0943-5ba1-4346-b572-ed66df3fe918.png)

ここまででエージェントの設定は完了です。


# サンプルコードの実行

ここからはエージェントのコードを作成、動作させる手順です。Python環境で実行しますのでData Science Serviceのターミナル画面に戻ります。

再度、今回利用するConda仮想環境がactivate状態になっているかどうかを確認してください。

```bash
(/home/datascience/conda/python_p312_any_x86_64_v1) bash-4.4$ conda env list

# conda environments:
#
                     * /home/datascience/conda/python_p312_any_x86_64_v1
base                   /opt/conda
odscruntimeconfig      /opt/conda/envs/odscruntimeconfig
```

この仮想環境に下記コマンドで必要なライブラリ(ADK)をインストールします

```bash
pip install -U pip "oci[adk]"
```

今回のコードを実行する際のワークディレクトリを作成します。

```bash
mkdir ~/agents
cd ~/agents
```

下記コードのagent_endpoint_idを前の手順でメモ帳に控えたOCIDに変更し、quickstart.pyとして保存してください。

💡: ブラウザ上ではコピペすると文字化けしていますが、保存後にcatすると問題なく表示されるため問題ありません。


```python
from typing import Dict
from oci.addons.adk import Agent, AgentClient, tool

# Use @tool to signal that this Python function is a function tool.
# Apply standard docstring to provide function and parameter descriptions.
@tool
def get_weather(location: str) -> Dict[str, str]:
    """
    指定した場所の天気を取得します。


    Args:
      location(str): 天気情報を取得する場所
    """
    return {"location": location, "temperature": 72, "unit": "F"}


def main():
    # Create an agent client with your authentication and region details
    # Replace the auth_type with your desired authentication method.
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="us-chicago-1",
    )

    # Create a local agent object with the client, instructions, and tools.
    # You also need the agent endpoint id. To obtain the OCID, follow Step 1.
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.xxxxxxxxxxxx",
        instructions="ツールを使用して天気予報のクエリを実行します。",
        tools=[get_weather]
    )

    # Sync local instructions and tools to the remote agent resource
    # You only need to invoke setup() when you change instructions and tools
    agent.setup()

    # Run the agent. You can embed this method in your webapp, slack bot, etc.
    # You invoke the run() when you need to handle your user's request.
    input = "シアトルは寒いですか？"
    response = agent.run(input)

    # Print the response
    response.pretty_print()

if __name__ == "__main__":
    main()
```

下記pythonコマンドで保存したプログラムを実行します。

```python
python quickstart.py
```

実行結果は下記のようになります。

```python
(/home/datascience/conda/python_p312_any_x86_64_v1) bash-4.4$ python quickstart.py 
[07/03/25 09:45:00]  INFO     Checking integrity of agent details...                                                                                       
                     INFO     Checking synchronization of local and remote agent settings...                                                               
                     INFO     Agent settings are not synchronized. Updating remote agent settings                                                          
[07/03/25 09:45:05]  INFO     Waiting for agent ocid1.genaiagent.oc1.us-chicago-1.amaaaaaal7l2mtaasrralfgy5xukqnohfstkw7eg2whfy4hblp55isdquoda to be       
                              active...                                                                                                                    
[07/03/25 09:45:10]  INFO     Waiting for agent ocid1.genaiagent.oc1.us-chicago-1.amaaaaaal7l2mtaasrralfgy5xukqnohfstkw7eg2whfy4hblp55isdquoda to be       
                              active...                                                                                                                    
[07/03/25 09:45:15]  INFO     Waiting for agent ocid1.genaiagent.oc1.us-chicago-1.amaaaaaal7l2mtaasrralfgy5xukqnohfstkw7eg2whfy4hblp55isdquoda to be       
                              active...                                                                                                                    
                     INFO     Checking synchronization of local and remote function tools...                                                               
╭─ Local and remote function tools found ─╮
│ Local function tools (1):               │
│ ['get_weather']                         │
│                                         │
│ Remote function tools (0):              │
│ []                                      │
╰─────────────────────────────────────────╯
                     INFO     Adding local tool get_weather to remote...                                                                                   
[07/03/25 09:45:20]  INFO     Waiting for tool ocid1.genaiagenttool.oc1.us-chicago-1.amaaaaaal7l2mtaagtuqwhvzbmd2bat5gitfxobpcpdcqpt4dq7bhxqhwzdq to be    
                              active...                                                                                                                    
[07/03/25 09:45:25]  INFO     Waiting for tool ocid1.genaiagenttool.oc1.us-chicago-1.amaaaaaal7l2mtaagtuqwhvzbmd2bat5gitfxobpcpdcqpt4dq7bhxqhwzdq to be    
                              active...                                                                                                                    
[07/03/25 09:45:26]  INFO     Checking synchronization of local and remote RAG tools...                                                                    
╭──────────────────────────────────── Chat request to remote agent ─────────────────────────────────────╮
│ (Local --> Remote)                                                                                    │
│                                                                                                       │
│ user message:                                                                                         │
│ シアトルは寒いですか？                                                                                │
│                                                                                                       │
│ performed actions by client:                                                                          │
│ []                                                                                                    │
│                                                                                                       │
│ session id:                                                                                           │
│ ocid1.genaiagentsession.oc1.us-chicago-1.amaaaaaa7mjirbaayqubozv52jvx4brxxlaabmdl4irl53a6knp7lgxewheq │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭────────────────── Chat response from remote agent ──────────────────╮
│ (Local <-- Remote)                                                  │
│                                                                     │
│ agent message:                                                      │
│ null                                                                │
│                                                                     │
│ required actions for client to take:                                │
│ [                                                                   │
│     {                                                               │
│         "action_id": "aac56145-7724-4689-a50a-d8011d63ab37",        │
│         "required_action_type": "FUNCTION_CALLING_REQUIRED_ACTION", │
│         "function_call": {                                          │
│             "name": "get_weather",                                  │
│             "arguments": "{\"location\": \"Seattle\"}"              │
│         }                                                           │
│     }                                                               │
│ ]                                                                   │
╰─────────────────────────────────────────────────────────────────────╯
╭─ Function call requested by agent and mapped local handler function ─╮
│ Agent function tool name:                                            │
│ get_weather                                                          │
│                                                                      │
│ Agent function tool call arguments:                                  │
│ {'location': 'Seattle'}                                              │
│                                                                      │
│ Mapped local handler function name:                                  │
│ get_weather                                                          │
╰──────────────────────────────────────────────────────────────────────╯
╭─────── Obtained local function execution result ────────╮
│ {'location': 'Seattle', 'temperature': 72, 'unit': 'F'} │
╰─────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Chat request to remote agent ─────────────────────────────────────╮
│ (Local --> Remote)                                                                                    │
│                                                                                                       │
│ user message:                                                                                         │
│ null                                                                                                  │
│                                                                                                       │
│ performed actions by client:                                                                          │
│ [                                                                                                     │
│     {                                                                                                 │
│         "action_id": "aac56145-7724-4689-a50a-d8011d63ab37",                                          │
│         "performed_action_type": "FUNCTION_CALLING_PERFORMED_ACTION",                                 │
│         "function_call_output": "{\"location\": \"Seattle\", \"temperature\": 72, \"unit\": \"F\"}"   │
│     }                                                                                                 │
│ ]                                                                                                     │
│                                                                                                       │
│ session id:                                                                                           │
│ ocid1.genaiagentsession.oc1.us-chicago-1.amaaaaaa7mjirbaayqubozv52jvx4brxxlaabmdl4irl53a6knp7lgxewheq │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────── Chat response from remote agent ────────────────────────────────╮
│ (Local <-- Remote)                                                                             │
│                                                                                                │
│ agent message:                                                                                 │
│ {                                                                                              │
│     "role": "AGENT",                                                                           │
│     "content": {                                                                               │
│         "text": "\u30b7\u30a2\u30c8\u30eb\u306f\u73fe\u5728\u300172\u00b0F\u3067\u3059\u3002", │
│         "citations": null,                                                                     │
│         "paragraph_citations": null                                                            │
│     },                                                                                         │
│     "time_created": "2025-07-03T09:45:29.951000+00:00"                                         │
│ }                                                                                              │
│                                                                                                │
│ required actions for client to take:                                                           │
│ null                                                                                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──── Agent run response ────╮
│ agent text message:        │
│ シアトルは現在、72°Fです。 　│
╰────────────────────────────╯
(base) bash-4.4$ 
```

「Agent run response」のメッセージが出力されていれば成功です。


# その他のワークロード

quickstartは非常にシンプルなコードになりましたが、実際のプロダクションシステムではADKを使ってより複雑なタスクを実行することになると思います。

そのベースとして、その他の典型的なワークロードのサンプルコードがありますのでこちらも併せて実施していただければと思います。

|項番| ワークロード | 概要 |
|-------|-------|-------|
|1| Function Tool | カスタム関数ツールを使用してエージェントを作成する方法を学習します。| 
|2| RAG Tool | 事事前構築済のRAGツールを使用してエージェントを作成する方法について学習します。 |
|3| Multiple Tools | 複数のツールを使用するエージェントを作成する方法について学習します。| 
|4| Multi-Turn Conversations | 会話セッションを切り替えてもコンテキストを維持するエージェントを作成する方法について学習します。| 
|5| Multi-Agent Collaboration |Supervisor-Collaboratorタイプのマルチエージェント構成について学習します。| 
|6| Deterministic Workflow | エージェントを使用した確定的マルチステップ・ワークフローの作成方法について学習します。 | 
|7| Life Cycle Hooks | ライフサイクル・フックを使用したエージェント実行の監視およびデバッグ。 | 
|8| Delete Sessions| セッションを事前に削除して、プライバシーとスケーラビリティを向上させます。 | 

複雑なタスクを実行するAIエージェントのワークロードのベースとなるサンプルコードは３、５、６になりますのでこちらの実行を推奨いたします。

各サンプルコードの実行手順は[こちら](https://docs.oracle.com/ja-jp/iaas/Content/generative-ai-agents/adk/api-reference/examples.htm)をご参照ください。