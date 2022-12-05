import json, requests
from peopledatalabs import PDLPY

class FetchProfileData:
    def __init__(self, user_full_name, user_email) -> None:
        self.api_key_file_path = 'api_key.txt'
        self.user_full_name = user_full_name
        self.user_email = user_email

        with open(self.api_key_file_path, 'r') as api_key_file:
            self.api_key = api_key_file.read()
        self.CLIENT = PDLPY(api_key=self.api_key)

        self.params = {
                        "api_key": self.api_key,
                        "name": self.user_full_name,
                        "email": self.user_email,
                        'titlecase': True
                        }

    def get_profile(self):
        PDL_URL = "https://api.peopledatalabs.com/v5/person/enrich"
        # json_response = self.CLIENT.person.enrichment(**self.params).json()
        json_response = requests.get(PDL_URL, params=self.params).json()
        if json_response['status'] == 200:
            record = json_response['data']

            self.final_record = {
                                    'full_name': record['full_name'],
                                    'gender': record['gender'],
                                    'birth_year': record['birth_year'],
                                    'linkedin_url': record['linkedin_url'],
                                    'current_job_company': record['job_company_name'],
                                    'current_job_title': record['job_title'],
                                    'current_location_state': record['location_region'],
                                    'current_location_country': record['location_country'],
                                    'skills': record['skills'],
                                    'experiences': record['experience'],
                                    'education': record['education']
                                }
            return self.clean_data()
        else:
            return 'error'

    def clean_data(self):
        profile_data = self.final_record
        print(profile_data)
        # Format data
        usable_data = {}

        # General profile details
        usable_data['ID'] = 9999999
        usable_data['name'] = profile_data['full_name']
        usable_data['gender'] = profile_data['gender']
        usable_data['birth_year'] = profile_data['birth_year']
        usable_data['linkedin_url'] = profile_data['linkedin_url']
        usable_data['current_job_company'] = profile_data['current_job_company']
        usable_data['current_job_title'] = profile_data['current_job_title']
        usable_data['current_location_state'] = profile_data['current_location_state']
        usable_data['current_location_country'] = profile_data['current_location_country']
        usable_data['skills'] = profile_data['skills']
        usable_data['experiences'] = {}
        usable_data['education'] = {}
        company_name_list = []

        # Work experience
        for experience in profile_data['experiences']:
            if experience['company'] is None:
                continue
            company_name = experience['company']['name']
            usable_data['experiences'][company_name] = []

        for experience in profile_data['experiences']:
            if experience['company'] is None:
                continue
            company_name = experience['company']['name']
            roles = {}
            roles['title'] = experience['title']['name']
            roles['start_date'] = experience['start_date']
            roles['end_date'] = experience['end_date']
            roles['presently_working'] = experience['is_primary']

            usable_data['experiences'][company_name].append(roles)

        # Education
        if profile_data['education']:
            for education in profile_data['education']:
                if education['school'] is None:
                    continue
                institution = education['school']['name']
                data = {}
                data['degrees'] = education['degrees']
                data['start_date'] = education['start_date']
                data['end_date'] = education['end_date']
                data['major'] = education['majors']
                data['gpa'] = education['gpa']
                data['location'] = education['school']['location']

                usable_data['education'][institution] = data

        return usable_data



# import json
# from peopledatalabs import PDLPY

# class FetchProfileData:
#     def __init__(self, user_full_name, user_email) -> None:
#         self.api_key_file_path = 'api_key.txt'
#         self.user_full_name = user_full_name
#         self.user_email = user_email

#         with open(self.api_key_file_path, 'r') as api_key_file:
#             self.api_key = api_key_file.read()
#         self.CLIENT = PDLPY(api_key=self.api_key)

#         self.params = {
#             "name": [self.user_full_name],
#             "email": [self.user_email],
#             'titlecase': True
#         }

#     def get_profile(self):
#         json_response = self.CLIENT.person.enrichment(**self.params).json()

#         if json_response['status'] == 200:
#             record = json_response['data']

#             self.final_record = {
#                                     'full_name': record['full_name'],
#                                     'gender': record['gender'],
#                                     'birth_year': record['birth_year'],
#                                     'linkedin_url': record['linkedin_url'],
#                                     'current_job_company': record['job_company_name'],
#                                     'current_job_title': record['job_title'],
#                                     'current_location_state': record['location_region'],
#                                     'current_location_country': record['location_country'],
#                                     'skills': record['skills'],
#                                     'experiences': record['experience'],
#                                     'education': record['education']
#                                 }
#             return self.clean_data()
#         else:
#             return 'error'

#     def clean_data(self):
#         profile_data = self.final_record

#         # Format data
#         usable_data = {}

#         # General profile details
#         usable_data['ID'] = 9999999
#         usable_data['name'] = profile_data['full_name']
#         usable_data['gender'] = profile_data['gender']
#         usable_data['birth_year'] = profile_data['birth_year']
#         usable_data['linkedin_url'] = profile_data['linkedin_url']
#         usable_data['current_job_company'] = profile_data['current_job_company']
#         usable_data['current_job_title'] = profile_data['current_job_title']
#         usable_data['current_location_state'] = profile_data['current_location_state']
#         usable_data['current_location_country'] = profile_data['current_location_country']
#         usable_data['skills'] = profile_data['skills']
#         usable_data['experiences'] = {}
#         usable_data['education'] = {}
#         company_name_list = []

#         # Work experience
#         for experience in profile_data['experiences']:
#             company_name = experience['company']['name']
#             usable_data['experiences'][company_name] = []

#         for experience in profile_data['experiences']:
#             company_name = experience['company']['name']
#             roles = {}
#             roles['title'] = experience['title']['name']
#             roles['start_date'] = experience['start_date']
#             roles['end_date'] = experience['end_date']
#             roles['presently_working'] = experience['is_primary']

#             usable_data['experiences'][company_name].append(roles)

#         # Education
#         for education in profile_data['education']:
#             institution = education['school']['name']
#             data = {}
#             data['degrees'] = education['degrees']
#             data['start_date'] = education['start_date']
#             data['end_date'] = education['end_date']
#             data['major'] = education['majors']
#             data['gpa'] = education['gpa']
#             data['location'] = education['school']['location']

#             usable_data['education'][institution] = data

#         return usable_data
