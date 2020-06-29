__author__ = "Thomas McGinn"
__credits__ = ["Thomas McGinn"]
__version__ = "0.0.5"
__maintainer__ = "Thomas McGinn"
__email__ = "thomas.mcginn@dexcom.com"
__status__ = "Production"

from search import Search

class G6_14_Day(Search):
    def __init__(self):
        super().__init__()
        self.title = ['G6_14_Day'.lower()]
        self.Path_ = [r'Z:\QA\Data Analysis\G6 14 Day']
        self.Parent_landing_page_path = ['#']
        self.Landing_page_path = ['#']
        self.Repository_path = [r'C:\Users\[username]\Desktop\Customer-Advocacy-Searches/blob/master/Library/Complaints/g6_pro.py']
        self.Github_repository_path = [r'https://github.com/dexcom-inc/Customer-Advocacy-Searches/blob/master/Library/Complaints/g6_14_day.py']
        self.Short_description = ['Testing Data']
        self.Long_description = ['#']
        self.Long_description_html = ['#']
        self.Technical_description = ['#']
        self.Databases_used = ['customer_advocacy_pms']
        self.Technical_databases_used = ['#']
        self.Created_by = [__author__]
        self.Maintained_by = [__maintainer__]
        self.Maintained_by_backup = ['#']

    def upload_doc_string_to_mysql(self, title = None, Path_ = None, Parent_landing_page_path = None, Landing_page_path = None, Repository_path = None, Github_repository_path = None, Short_description = None, Long_description = None, Long_description_html = None, Technical_description = None, Databases_used = None, Technical_databases_used = None, Created_by = None, Maintained_by = None, Maintained_by_backup = None):
        title = ''.join(self.title)
        Path_ = ''.join(self.Path_)
        Parent_landing_page_path = ''.join(self.Parent_landing_page_path)
        Landing_page_path = ''.join(self.Landing_page_path)
        Repository_path = ''.join(self.Repository_path)
        Github_repository_path = ''.join(self.Github_repository_path)
        Short_description = ''.join(self.Short_description)
        Long_description = ''.join(self.Long_description)
        Long_description_html = ''.join(self.Long_description_html)
        Technical_description = ''.join(self.Technical_description)
        Databases_used = ''.join(self.Databases_used)
        Technical_databases_used = ''.join(self.Technical_databases_used)
        Created_by = ''.join(self.Created_by)
        Maintained_by = ''.join(self.Maintained_by)
        Maintained_by_backup = ''.join(self.Maintained_by_backup)
        con = Search.test_con.connect()
        sql_insert = "insert into test values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)
        sql_update = "on duplicate key update Path_ = '{}', Parent_landing_page_path = '{}', Landing_page_path = '{}', Repository_path = '{}', Github_repository_path = '{}', Short_description = '{}', Long_description = '{}', Long_description_html = '{}', Technical_description = '{}', Databases_used = '{}', Technical_databases_used = '{}', Created_by = '{}', Maintained_by = '{}', Maintained_by_backup = '{}'".format(Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)
        sql_upload = sql_insert + ' ' + sql_update
        con.execute(sql_upload) 

G6_14_Day().upload_doc_string_to_mysql()

