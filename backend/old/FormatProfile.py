import random
from datetime import datetime
import pycountry_convert as pc

class FormatData:

    def __init__(self, profile):
        self.profile = profile

    def format_date(self, role_date):
        format = '%Y-%m'
        return datetime.strptime(role_date, format)

    def get_n_pos(self):
        n_pos = 0
        for experience in self.profile.get('experiences'):
            n_pos += len(self.profile.get('experiences')[experience])
        return n_pos

    def get_avg_n_pos_per_prev_tenure(self):
        num_experiences = len(self.profile.get('experiences'))
        n_pos = self.get_n_pos()

        return (n_pos/num_experiences)

    def get_avg_pos_len(self):
        n_days = 0
        n_pos = self.get_n_pos()

        for experience in self.profile.get('experiences'):
            for roles in self.profile.get('experiences')[experience]:

                start_date = self.format_date(roles['start_date'])
                if roles['end_date'] is None:
                    end_date = self.format_date(str(datetime.now())[:7])
                else:
                    end_date = self.format_date(roles['end_date'])
                n_days += (end_date - start_date).days

        return (n_days / n_pos)

    def get_n_prev_tenures(self):
        n_prev_tenures = len(self.profile.get('experiences'))
        return n_prev_tenures

    def get_avg_prev_tenure_len(self, get_tenure_len=False):

        first_experience = list(self.profile.get('experiences').keys())[0]

        min_start_date = self.format_date(str(datetime.now())[:7])

        if self.profile.get('experiences')[first_experience][0]['end_date'] is None:
            max_end_date = self.format_date(str(datetime.now())[:7])
        else:
            max_end_date = self.format_date(self.profile.get('experiences')[first_experience][0]['end_date'])

        for experience in self.profile.get('experiences'):

            for roles in self.profile.get('experiences')[experience]:
                start_date = self.format_date(roles['start_date'])
                if roles['end_date'] is None:
                    end_date = self.format_date(str(datetime.now())[:7])
                else:
                    end_date = self.format_date(roles['end_date'])

                if start_date < min_start_date:
                    min_start_date = start_date

                if end_date > max_end_date:
                    max_end_date = end_date

        tenure_len = (max_end_date - min_start_date).days

        if get_tenure_len:
            return tenure_len

        return (tenure_len / self.get_n_prev_tenures())

    def get_age(self):

        if self.profile.get('birth_year') is None:
            for education in self.profile.get('education'):
                if "Bachelors" in self.profile.get('education')[education]['degrees']:
                    bach_end_date = self.profile.get('education')[education]['end_date']
                    bach_end_year = datetime.strptime(bach_end_date, '%Y').year
                    today = datetime.now().year
                    age = today - bach_end_year + 22
                else:
                    age = 23
        else:
            today = datetime.now().year
            birth_year = datetime.strptime(self.profile.get('birth_year'), '%Y').year
            age = today - birth_year

        return age

    def get_gender(self):
        return self.profile.get('gender')

    def get_ethnicity(self):

        continent = None
        for education in self.profile.get('education'):
            if "Bachelors" in self.profile.get('education')[education]['degrees']:
                continent = self.profile.get('education')[education]['location']['continent']

        if continent is None:
            country = self.profile.get('current_location_country')
            country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
            continent = pc.country_alpha2_to_continent_code(country_code)

        if continent == "Asia":
            return 'Asian'
        elif continent == "Africa":
            return "Black"
        elif continent in ["Europe", "North America", "South America", "Russia", "Antartica", "Australia"]:
            return "White"

    def get_n_followers(self):
        return random.randint(0, 500)

    def get_test_data_format(self):
        test_dict = {}

        # avg_n_pos_per_prev_tenure
        test_dict['avg_n_pos_per_prev_tenure'] = self.get_avg_n_pos_per_prev_tenure()

        # avg_pos_len
        test_dict['avg_pos_len'] = self.get_avg_pos_len()

        # avg_prev_tenure_len
        test_dict['avg_prev_tenure_len'] = self.get_avg_prev_tenure_len()

        # n_pos
        test_dict['n_pos'] = self.get_n_pos()

        # n_prev_tenures
        test_dict['n_prev_tenures'] = self.get_n_prev_tenures()

        # tenure_len
        test_dict['avg_prev_tenure_len'] = self.get_avg_prev_tenure_len(get_tenure_len=True)

        # age
        test_dict['age'] = self.get_age()

        test_dict['african'] = 0.0
        test_dict['celtic_english'] = 0.0
        test_dict['east_asian'] = 0.0
        test_dict['european'] = 0.0
        test_dict['greek'] = 0.0
        test_dict['hispanic'] = 0.0
        test_dict['jewish'] = 0.0
        test_dict['muslim'] = 0.0
        test_dict['nordic'] = 0.0
        test_dict['south_asian'] = 0.0

        # n_followers
        test_dict['n_followers'] = self.get_n_followers()

        # gender
        gender = self.get_gender()
        if gender == "Male":
            test_dict['gender_Female'] = 0
            test_dict['gender_Male'] = 1

        else:
            test_dict['gender_Female'] = 1
            test_dict['gender_Male'] = 0

        # ethinicity
        ethnicity = self.get_ethnicity()
        if ethnicity == "Asian":
            test_dict['ethnicity_Asian'] = 1
            test_dict['ethnicity_Black'] = 0
            test_dict['ethnicity_White'] = 0
        elif ethnicity == "Black":
            test_dict['ethnicity_Asian'] = 0
            test_dict['ethnicity_Black'] = 0
            test_dict['ethnicity_White'] = 1
        else:
            test_dict['ethnicity_Asian'] = 0
            test_dict['ethnicity_Black'] = 1
            test_dict['ethnicity_White'] = 0

        return test_dict
