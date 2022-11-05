
.. _manual-docs:

========================
マニュアル・ドキュメント
========================

.. contents:: 目次
  :local:
  :depth: 1

はじめに
========

本マニュアルは `Sphinx <https://www.sphinx-doc.org/ja/master/index.html>`_ と呼ばれるドキュメントフレームワークで作成される．
ソースファイルは Git で管理され，そのリモートリポジトリは `GitHub <https://github.com/Akafumi/imasaba_sg>`_ 上で管理される．

:ドキュメントの執筆に必要なもの:

  * Sphinx 文章をビルドできるホスト
  * GitHub アカウント
  * discord
  * 公開サーバ(現状は計算機 ``NEMO`` )の管理者アカウント

  .. hint:: 

    * `reStructuredText <https://www.sphinx-doc.org/ja/master/usage/restructuredtext/index.html>`_ 
    * `Sphinxでの文章の書き方(reStructuredText) <https://planset-study-sphinx.readthedocs.io/ja/latest/04.html>`_ 
    * `サルでもわかる Git 入門 <https://backlog.com/ja/git-tutorial/>`_ 

執筆規則
========

マニュアル執筆の原則
--------------------

* 可能な限り簡潔に書く
* 個々の文の解釈が唯一となるように書く
* 1つの文で伝えることは1つだけにする

表記
----

文の表現・丁寧語・謙譲語・尊敬語
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本文章は，言い切りの形を基本とする．
マニュアルなので，チャットやメール，広報の文章とは異なり，謙譲語・尊敬語は原則として用いない．

  .. hint:: 

      * ``ご覧ください`` -> ``参照``
      * ``ご入力ください`` -> ``入力する`` or ``入力``

句読点
^^^^^^

以下のような日本語論文スタイルにする．

  +------------------+------------------------------------+
  | **日本語の句点** | ``．`` (全角ピリオド)              |
  +------------------+------------------------------------+
  | **日本語の読点** | ``，`` (全角カンマ)                |
  +------------------+------------------------------------+
  | **英文**         | ``.`` ``,`` (半角ピリオド，カンマ) |
  +------------------+------------------------------------+

カタカナ語
^^^^^^^^^^

英単語として分かれるものは，・ または半角スペースを入れる．

スクリーン・ショットの掲載
^^^^^^^^^^^^^^^^^^^^^^^^^^

``image`` ディレクティブではなく， ``figure`` ディレクティブを使う．
( ``image`` ディレクティブを使うと，殆どのスタイルで画像の前後スペースが変になる場合が多い．)


Sphinx ビルド環境
=================

計算機 NEMO の環境を使う
------------------------

計算機 NEMO には Sphinx 文章のビルドに必要なツールがインストールしてある．

新しい計算機に構築する
----------------------

Sphinx で構築された文章をビルドするためには， Python (3.7 以上) が必要である．
加えて，以下の  Python Package (PyPl) を ``pip`` コマンドでインストールする必要がある．

.. code-block:: bash

  pip3 install Sphinx sphinx-intl sphinx-rtd-theme sphinxcontrib-actdiag sphinxcontrib-applehelp sphinxcontrib-blockdiag sphinxcontrib-devhelp sphinxcontrib-htmlhelp sphinxcontrib-jsmath sphinxcontrib-nwdiag sphinxcontrib-qthelp sphinxcontrib-seqdiag sphinxcontrib-serializinghtml sphinxcontrib-websupport

インストール後，以下のコマンドで確認できる．

.. code-block:: bash

  sphinx-build --version


