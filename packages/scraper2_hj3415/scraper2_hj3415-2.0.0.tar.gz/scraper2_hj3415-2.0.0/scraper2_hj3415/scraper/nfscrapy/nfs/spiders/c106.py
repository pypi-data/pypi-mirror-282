import time
import scrapy
import pandas as pd
import selenium.common.exceptions
from utils_hj3415 import utils
from scrapy.selector import Selector

from nfs import items
from nfs.spiders import common

# 분기와 년도 2페이지를 스크랩함.


class C106Spider(scrapy.Spider):
    name = 'c106'
    allowed_domains = ['navercomp.wisereport.co.kr']
    WAIT = 2

    def __init__(self, code, mongo_client, *args, **kwargs):
        super(C106Spider, self).__init__(*args, **kwargs)
        self.codes = common.adjust_arg_type(code)
        self.mongo_client = mongo_client
        self.driver = utils.get_driver()

    def start_requests(self):
        total_count = len(self.codes)
        print(f'Start scraping {self.name}, {total_count} items...')
        self.logger.info(f'entire codes list - {self.codes}')
        for i, one_code in enumerate(self.codes):
            print(f'{i + 1}/{total_count}. Parsing {self.name}...{one_code}')
            # C106의 컬럼명을 얻기 위한 주소
            yield scrapy.Request(url=f'https://navercomp.wisereport.co.kr/v2/company/c1060001.aspx?cmp_cd={one_code}',
                                 callback=self.parse_c106_col,
                                 cb_kwargs=dict(code=one_code)
                                 )

    def parse_c106_col(self, response, code):
        self.driver.get(response.url)
        # 경험상 1초는 데이터 수집에러 가능성 있었음.
        time.sleep(self.WAIT)
        try:
            html = Selector(text=self.driver.page_source)
        except selenium.common.exceptions.UnexpectedAlertPresentException:
            self.logger.warning("Parsing error ... maybe 올바른 종목이 아닙니다.")
        else:
            # 컬럼명을 얻어 다음 request에 실어 보낸다.
            cols = []
            for i in range(1, 7):
                pretitle = html.xpath(f'//*[@id="cTB611_h"]/thead/tr/th[{i}]/text()[1]').getall()[0].strip().replace('.','')
                # 인덱스에 공칸일 경우 데이터베이스 저장시 에러가 발생하기 때문에 추가한 코드
                if pretitle == '':
                    pretitle = 'Unnamed'
                cols.append(pretitle)
            self.logger.info(f'Parsing column names - {code} >>>> {cols}')

            titles = ['y', 'q'] # pipeline에서 테이블명으로 됨
            for title in titles:
                # C106의 내부의 iframe주소, 분기와 연간 2개임
                # reference from https://docs.scrapy.org/en/latest/topics/request-response.html (request 연쇄보내기)
                yield scrapy.Request(
                    url=f'https://navercomp.wisereport.co.kr/company/cF6002.aspx?cmp_cd={code}'
                        f'&finGubun=MAIN&cmp_cd1=&cmp_cd2=&cmp_cd3=&cmp_cd4=&sec_cd=G453010&frq={title.upper()}',
                    callback=self.parse_c106,
                    cb_kwargs=dict(code=code, cols=cols, title=title)
                )

    def parse_c106(self, response, code, cols, title):
        df = C106Spider.get_df_from_html(response.text, cols)
        df['항목'] = (df['항목'].str.replace('\(억\)', '', regex=True).str.replace('\(원\)', '', regex=True)
                    .str.replace('\(억원\)', '', regex=True).str.replace('\(%\)', '', regex=True))
        self.logger.info(df)
        # make item to yield
        item = items.C106items()
        item['코드'] = code
        item['title'] = title
        item['df'] = df
        yield item

    @staticmethod
    def get_df_from_html(html, cols):
        # 전체 html source에서 table 부위만 추출하여 데이터프레임으로 변환
        df = pd.read_html(html)[0]
        # 인덱스 추가
        df.columns = cols
        df.dropna(how='all', inplace=True)
        return df

    def __str__(self):
        return 'C106 Spider'

    def __del__(self):
        if self.driver is not None:
            print('Retrieve chrome driver...')
            self.driver.quit()


