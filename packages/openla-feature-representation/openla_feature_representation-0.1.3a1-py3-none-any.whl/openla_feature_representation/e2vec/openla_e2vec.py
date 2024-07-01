import numpy as np
import pandas as pd
import datetime as dt
import fasttext as ft
import OpenLA as la
import time
import re

Operation_dict = {
    "NEXT": "N",
    "PREV": "P",
    "ADD MARKER": "A",
    "OPEN": "O",  
    "CLOSE": "C",  
    "PAGE_JUMP": "J", 
    "GETIT": "G",  
    "DELETE MARKER": "E",
    "BOOKMARK_JUMP": "E",
    "ADD BOOKMARK": "E",
    "NOTGETIT": "E",
    "ADD MEMO": "E",
    "MEMO_TEXT_CHANGE_HISTORY": "E",
    "DELETE BOOKMARK": "E",
    "CHANGE MEMO": "E",
    "SEARCH_JUMP": "E",
    "REGIST CONTENTS": "E",
    "DELETE_MEMO": "E",
    "SEARCH": "E",
    "OPEN_RECOMMENDATION": "E",
    "CLICK_RECOMMENDATION": "E",
    "TIMER_PAUSE": "E",
    "TIMER_STOP": "E",
    "ADD_HW_MEMO": "E",
    "CLOSE_RECOMMENDATION": "E",
    "CLEAR_HW_MEMO": "E",
    "LINK_CLICK": "E",
    "UNDO_HW_MEMO": "E",
    "ADD_RECOMMENDATION": "E",
    "REDO_HW_MEMO": "E",
    "DELETE_RECOMMENDATION": "E",
}


class E2Vec(object):
    # 初期化
    def __init__(
        self,
        fastText_model,
        EduData,
        course_id,
        SorU="user",
        dict=Operation_dict,
        word_time=1,
    ):
        self._fT_model = ft.load_model(fastText_model)
        self._SorU = SorU
        self._dict = Operation_dict
        self._word_time = word_time
        self._course_info = la.CourseInformation(files_dir=EduData, course_id=course_id)
        self._eventstream = self._course_info.load_eventstream()
        self._all_user_vec = []
        self._all_sentence_vec = []
        self._back_up = self._course_info
        self._course_id = course_id

    # デバッグ用
    # def _print(self):
    #  print(self._course_info.lecture_start_time(3))

    # オペレーション間の時間を文字化する
    def _interval_check(self, interval_sec: int):
        if interval_sec <= 1:
            interval_word = ""
        elif interval_sec > 1 and interval_sec <= 10:
            interval_word = "s"
        elif interval_sec > 10 and interval_sec <= 300:
            interval_word = "m"
        else:
            interval_word = "l"
        return interval_word

    # 入力useridのイベントストリームを抽出
    # contentsid，eventtimeでsort
    def _get_user_eventstream(self, userid):
        user_stream = la.select_user(self._eventstream, user_id=userid)
        user_stream_df = user_stream.df.sort_values(["contentsid", "eventtime"])
        user_stream_df = user_stream_df[["contentsid", "operationname", "eventtime"]]
        df = user_stream_df.replace(self._dict)
        df.index = np.arange(0, len(df))
        return df

    # ユーザーごとのイベントストリームからsentenceを生成する
    def _get_oneuser_sentences(self, user_eventstream_df:pd.DataFrame,word_max_len=15)->str:
        """
        To generate sentence(action) from user_eventstream.
        改行条件:
        1. contentsidが変化した場合
        2. interval_wordがlの場合(5分以上オペレーション間の時間が空いた場合)
        単語の分割条件:
        1. 単語の長さがword_max_len以上になった場合
        2. 単語の先頭から1分以上たった場合
        params:
        user_event_stream_df : ユーザーごとのイベントストリーム
        word_max_len : 単語の最大長さ。これ以上になったら、強制的に分割する
    
        return:
        sentences : user_event_streamをsentencesに変換したもの
        """
    
        sentences = "" #返り値用の変数
        word = "" #単語作成用の一時変数
        user_eventstream_df = user_eventstream_df.reset_index(drop=True) #indexを0始まりに直す
        for index, data in user_eventstream_df.iterrows():
            current = dt.datetime.strptime((data["eventtime"]), '%Y-%m-%d %H:%M:%S') #word_timeによる条件の作動のための変数 
            current_contents_id = data["contentsid"] #現在のコンテンツID

            if index == 0:#初期化処理
                previous = current 
                previous_contents_id = current_contents_id #最初はpreviousも同じにする
                start = current
                end = start + dt.timedelta(minutes=self._word_time)

            if (previous_contents_id != current_contents_id):#コンテンツがIDが変わった場合
                sentences += word + "\n"
                word = ""
                current = dt.datetime.strptime(data["eventtime"], '%Y-%m-%d %H:%M:%S')
                start = current
                end = start + dt.timedelta(minutes=self._word_time)
            else:   
                #前のログからの時間を計算して、該当文字を追加
                current_contents_id = data["contentsid"]
                current = dt.datetime.strptime(data["eventtime"], '%Y-%m-%d %H:%M:%S')
                interval_sec = current - previous
                interval_sec = interval_sec.seconds
                interval_word = self._interval_check(interval_sec)
                word += interval_word

                if interval_word == "l":#長時間ログが空いた場合の処理
                    sentences += word + "\n"
                    word = ""
                    current = dt.datetime.strptime(data["eventtime"], '%Y-%m-%d %H:%M:%S')
                    start = current
                    end = start + dt.timedelta(minutes=self._word_time)
                
                if len(word) >= word_max_len - 1: #最大単語数による分割のチェック
                    sentences += word + "_ "
                    word = ""
                    current = dt.datetime.strptime(data["eventtime"], '%Y-%m-%d %H:%M:%S')
                    start = current
                    end = start + dt.timedelta(minutes=self._word_time)

                
                if current > end: # wordの先頭から一定時間以上のログ(新しい単語の先頭になるログ)
                    sentences += word + " "
                    word = ""
                    current = dt.datetime.strptime(data["eventtime"], '%Y-%m-%d %H:%M:%S')
                    start = current
                    end = start + dt.timedelta(minutes=self._word_time)

            #wordへの単語の追加
            word += data["operationname"]

            #各種変数の更新処理
            previous = current
            previous_contents_id = current_contents_id

        else: #最後はwordを追加
            sentences += word

        if sentences != "":
            sentences += "\n"
        
        return sentences 

    # センテンス生成用呼び出しモジュール
    def _get_learninglog_sentences(self, userid):
        user_eventstream_df = self._get_user_eventstream(userid)
        return self._get_oneuser_sentences(user_eventstream_df)

    # ファイル書き出し
    def _write_sentences(self, file_path, sentences):
        f = open(file_path, "w")
        for sentence in sentences:
            if sentence != None:
                f.write(sentence)
                if self._SorU == "user":
                    f.write("****user****\n")
        f.close()

    # ベクトル書き出し
    def _write_vector(vector: np.ndarray, VectorFilePath):
        vecs_df = pd.DataFrame(vector)
        vecs_df.to_csv(VectorFilePath, index=False)

    # 　sentence生成
    def get_sentences(self, file_path):
        usersid = self._eventstream.user_id()
        sentences = [self._get_learninglog_sentences(userid) for userid in usersid]
        self._write_sentences(file_path, sentences)

    # 一時保存先の解放
    def _refresh(self):
        if len(self._all_user_vec) != 0:
            self._all_user_vec = []
        if len(self._all_sentence_vec) != 0:
            self._all_sentence_vec = []

    # 外部から呼び出し　sentence を入力として vector生成
    def sentences_to_vector(
        self,
        sentences_path,
        save_path,
        mode="all",
        start=None,
        period=None,
        select_weeks=None,
        cat_mode=None,
    ):
        tmp1 = []
        tmp2 = []
        week = ""
        self._refresh()
        if mode == "select":
            if select_weeks is None:
                week = "all"
            else:
                for week_i in select_weeks:
                    week += str(week_i)
            # save_path = re.sub('.csv', '_{}-{}_{}.csv'.format(self._start, self._start + self._period, week),save_path)
        if self._SorU == "user":
            with open(sentences_path, "r") as f:
                for sentence in f:
                    if sentence == "****user****\n":
                        if tmp1 != []:
                            tmp1 = np.sum(tmp1, axis=0)
                            self._all_user_vec.append(tmp1)
                            tmp1 = []
                        continue
                    else:
                        sentence = sentence.rstrip("\n")
                        tmp2 = self._fT_model.get_sentence_vector(sentence)
                        tmp1.append(tmp2)
            self._all_user_vec = np.array(self._all_user_vec)
            vecs_df = pd.DataFrame(self._all_user_vec)
            vecs_df["userid"] = self._index
            vecs_df.set_index("userid", inplace=True)
        elif self._SorU == "sentence":
            with open(sentences_path, "r") as f:
                for sentence in f:
                    sentence = sentence.rstrip("\n")
                    tmp2 = self._fT_model.get_sentence_vector(sentence)
                    self._all_sentence_vec.append(tmp2)
            vecs_df = pd.DataFrame(self._all_sentence_vec)
        if cat_mode == "time":
            # vecs_df.to_csv() ある周期のベクトルを保存したい場合
            return vecs_df
        elif cat_mode == "week":
            # vecs_df.to_csv()　ある周期のベクトルを保存したい場合
            return vecs_df
        else:
            # vecs_df.to_csv(save_path, index=self._index) #save_pathを入力として受け取っておく
            # return save_path                             pathを返したい場合
            return vecs_df
        return vecs_df  # DataFrameを返すのみの場合，if cat_mode 以下をなくしてここを実行すれば良い

    # 指定したタイミングの時間を計算して開始時間と終了時間を返す
    def _specific_time_extraction(self, start: int, period: int):
        start_end = []
        for i in range(len(self._course_info.lecture_time_df())):
            lecture_start_time = self._course_info.lecture_start_time(
                i + 1
            ) + dt.timedelta(minutes=start)
            lecture_end_time = lecture_start_time + dt.timedelta(minutes=period)
            start_end.append([lecture_start_time, lecture_end_time])
        return start_end

    # 特定の時間のイベントストリームを取得
    def _specifictime_eventstream(
        self, start_end: list, eventstream_path, select_weeks=None
    ):
        if select_weeks == None:
            select_weeks = [i + 1 for i in range(len(start_end))]
        select_time_df = pd.DataFrame()
        for lecture_week in select_weeks:
            selected_time = start_end[lecture_week - 1]
            one_select_time_df = la.data_extraction.select_time(
                self._eventstream,
                start_time=selected_time[0],
                end_time=selected_time[1],
            ).df
            select_time_df = pd.concat([select_time_df, one_select_time_df])
        select_time_df.to_csv(eventstream_path, index=False)

    # イベントストリーム置き換えモジュール(時間指定の時などに使用)
    def _replace_eventstream(self, eventstream_path, info_dir, course_id):
        self._course_info = la.CourseInformation(
            event_stream_file=eventstream_path,
            lecture_material_file=info_dir
            + "/Course_{}_LectureMaterial.csv".format(course_id),
            lecture_time_file=info_dir + "/Course_{}_LectureTime.csv".format(course_id),
            grade_point_file=info_dir + "/Course_{}_GradePoint.csv".format(course_id),
        )
        self._eventstream = self._course_info.load_eventstream()
        print(len(self._eventstream.df))

    # 外部から呼び出すモジュール 指定した条件に合うテキストファイル(sentences)を作成し，そのパスを出力とする．
    def get_Sentences(
        self,
        sentences_path,
        eventstream_path,
        info_dir,
        course_id,
        mode="all",
        start=0,
        period=90,
        select_weeks=None,
    ):
        if mode == "all":
            pass
        elif mode == "select":
            # sl_time0 = time.time()
            self._start = start
            self._period = period
            selcted_time = self._specific_time_extraction(start, period)
            self._specifictime_eventstream(selcted_time, eventstream_path, select_weeks)
            self._replace_eventstream(eventstream_path, info_dir, course_id)
            sentences_path_tmp = re.sub(
                ".txt", "{}-{}.txt".format(start, period + start), sentences_path
            )
            # sl_time1 = time.time()
            # print("select time log " + str(sl_time1 - sl_time0) + " seconds")
        usersid = self._eventstream.user_id()
        self._index = usersid
        # l2s_time0 = time.time()
        sentences = [self._get_learninglog_sentences(userid) for userid in usersid]
        # l2s_time1 = time.time()
        # print("log to sentences " + str(l2s_time1 - l2s_time0) + " seconds")
        if mode == "all":
            self._write_sentences(sentences_path, sentences)
            return sentences_path
        elif mode == "select":
            self._write_sentences(sentences_path_tmp, sentences)
            # 繰り返しの実行のために限定した設定の初期化
            self._course_info = self._back_up
            self._eventstream = self._course_info.load_eventstream()
            return sentences_path_tmp

    # 時間ごとに集約したベクトルを連結して出力
    def get_concat_vectors(
        self,
        sentences_path,
        eventstream_path,
        vector_path,
        info_dir,
        course_id,
        concat_mode="time",
        start=0,
        period=90,
        select_weeks=None,
    ):
        vec_df = pd.DataFrame()
        sub_vec_df = pd.DataFrame()
        lecture_time = self._course_info.lecture_end_time(
            1
        ) - self._course_info.lecture_start_time(1)
        lecture_time_minutes = int(lecture_time.seconds / 60)
        if concat_mode == "time":
            for i in range(int(lecture_time_minutes / period)):
                # ex0 = time.time()
                sentences_path_tmp = self.get_Sentences(
                    sentences_path,
                    mode="select",
                    start=start,
                    period=period,
                    eventstream_path=eventstream_path,
                    info_dir=info_dir,
                    course_id=course_id,
                    select_weeks=select_weeks,
                )
                # ex1 = time.time()
                sub_vec_df = self.sentences_to_vector(
                    sentences_path_tmp,
                    vector_path,
                    mode="select",
                    start=start,
                    period=period,
                    select_weeks=select_weeks,
                    cat_mode=concat_mode,
                )
                ex2 = time.time()
                # print('senetence '+ str(ex1-ex0) +' seconds')
                # print('vecotors '+ str(ex2-ex1) +' seconds')
                sub_vec_df["userid"] = self._index
                sub_vec_df.set_index("userid", inplace=True)
                self._course_info = self._back_up
                self._eventstream = self._course_info.load_eventstream()
                if sub_vec_df.empty:
                    continue
                sub_vec_df.columns = [
                    self._fT_model.get_dimension() * i + j
                    for j in range(self._fT_model.get_dimension())
                ]
                vec_df = pd.merge(
                    vec_df, sub_vec_df, left_index=True, right_index=True, how="outer"
                )
                start = start + period
                # user id を基準にconcatする必要がある
        elif concat_mode == "week":
            num_of_lecture = len(self._course_info.lecture_time_df())
            for i in range(num_of_lecture):
                one_week = [i + 1]
                sentences_path_tmp = self.get_Sentences(
                    sentences_path,
                    mode="select",
                    start=start,
                    period=lecture_time_minutes,
                    eventstream_path=eventstream_path,
                    info_dir=info_dir,
                    course_id=course_id,
                    select_weeks=one_week,
                )
                sub_vec_df = self.sentences_to_vector(
                    sentences_path_tmp,
                    save_path=vector_path,
                    mode="select",
                    start=0,
                    period=lecture_time_minutes,
                    select_weeks=one_week,
                    cat_mode=concat_mode,
                )
                self._course_info = self._back_up
                self._eventstream = self._course_info.load_eventstream()
                if sub_vec_df.empty:
                    print("eventstream in lecture {} is empty.".format(one_week[0]))
                    continue
                sub_vec_df["userid"] = self._index
                sub_vec_df.set_index("userid", inplace=True)
                # sub_vec_df.to_csv(r"C:\Users\miyazakiyuma\code\python\E2Vec\Vectors\Test-UserVectors_D-2022_1min_{}.csv".format(one_week))
                sub_vec_df.columns = [
                    self._fT_model.get_dimension() * i + j
                    for j in range(self._fT_model.get_dimension())
                ]
                vec_df = pd.merge(
                    vec_df, sub_vec_df, left_index=True, right_index=True, how="outer"
                )
        # ここまでを終えて，ログがなかった部分はNaNが入っていてそのままでは計算できないので，NaNを0に置換する
        vec_df = vec_df.fillna(0)
        # vector_path_con = re.sub('.csv', '_{}.csv'.format(concat_mode),vector_path)
        # vec_df.to_csv(vector_path_con)
        return vec_df
        # return vector_path_con

    def generate_sentences(
        self,
        sentences_dir_path,
        eventstream_file_path,
        input_csv_dir_path,
        course_id,
        use_timespan=False,
        start_minute=0,
        total_minutes=90,
        timespan_weeks=None,
    ):
        """Generates sentences from the events in the stream, using an
        artificial language. The sentences are persisted in a text file,
        and the function returns the path to this file.

        :param sentences_dir_path: Path to the directory where the file will be saved
        :type sentences_dir_path: str
        :param eventstream_file_path: Path to the EventStream CSV file
        :type eventstream_file_path: str
        :param input_csv_dir_path: Path to the directory where the datased is
        :type input_csv_dir_path: str
        :param course_id: Course identifier within the dataset
        :type course_id: str
        :param use_timespan: Whether to use the three following args, defaults to False
        :type use_timespan: bool, optional
        :param start_minute: The minute the analysis should start, defaults to 0
        :type start_minute: int, optional
        :param total_minutes: The number of minutes to analyze, defaults to 90
        :type total_minutes: int, optional
        :param timespan_weeks: A list of int numerals representing the relevant weeks within the course, defaults to None
        :type timespan_weeks: list, optional
        :return: Path to the text file with the generated sentences
        :rtype: str
        """
        return self.get_Sentences(
            sentences_dir_path,
            eventstream_file_path,
            input_csv_dir_path,
            course_id,
            mode="select" if use_timespan else "all",
            start=start_minute,
            period=total_minutes,
            select_weeks=timespan_weeks,
        )

    def vectorize_sentences(
        self,
        sentences_file_path,
    ):
        """Generates vectors from the provided sentences file.

        :param sentences_file_path: Path to the sentences file
        :type sentences_file_path: str
        :return: A DataFrame with the generated vectors
        :rtype: pandas.DataFrame
        """
        return self.sentences_to_vector(
            sentences_path=sentences_file_path,
            save_path="",
            mode="all",
        )

    def concatenate_vectors(
        self,
        sentences_dir_path,
        eventstream_file_path,
        input_csv_dir_path,
        course_id,
        by_weeks=False,
        start_minute=0,
        total_minutes=90,
        timespan_weeks=None,
    ):
        """Concatenate vectors by time (minutes) or weeks.

        :param sentences_dir_path: Path to the directory where the file will be saved
        :type sentences_dir_path: str
        :param eventstream_file_path: Path to the EventStream CSV file
        :type eventstream_file_path: str
        :param input_csv_dir_path: Path to the directory where the datased is
        :type input_csv_dir_path: str
        :param course_id: Course identifier within the dataset
        :type course_id: str
        :param by_weeks: Whether to concatenate by weeks, defaults to False (concatenate by time)
        :type by_weeks: bool, optional
        :param start_minute: The minute the analysis should start, defaults to 0
        :type start_minute: int, optional
        :param total_minutes: The number of minutes to analyze, defaults to 90
        :type total_minutes: int, optional
        :param timespan_weeks: A list of int numerals representing the relevant weeks within the course, defaults to None
        :type timespan_weeks: list, optional
        :return: A Dataframe with the cocatenated vectors
        :rtype: pandas.DataFrame
        """
        return self.get_concat_vectors(
            sentences_path=sentences_dir_path,
            eventstream_path=eventstream_file_path,
            vector_path="",
            info_dir=input_csv_dir_path,
            course_id=course_id,
            concat_mode="week" if by_weeks else "time",
            start=start_minute,
            period=total_minutes,
            select_weeks=timespan_weeks,
        )
