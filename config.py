import os
from datetime import timedelta

class Config:
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///learnhub.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Payment Configuration
    PAYMENT_GATEWAYS = {
        'payfast': {
            'merchant_id': os.getenv('PAYFAST_MERCHANT_ID'),
            'merchant_key': os.getenv('PAYFAST_MERCHANT_KEY'),
            'return_url': 'https://yourdomain.com/payment/success',
            'cancel_url': 'https://yourdomain.com/payment/cancel',
            'notify_url': 'https://yourdomain.com/payment/notify'
        },
        'yoco': {
            'secret_key': os.getenv('YOCO_API_KEY')
        }
    }
    
    # Bank Account Distribution
    PAYOUT_DISTRIBUTION = {
        'owner_capitec': 0.60,
        'ai_capitec': 0.20,
        'reserve_absa': 0.20
    }
    
    # Social Media APIs
    SOCIAL_MEDIA = {
        'facebook': {
            'access_token': os.getenv('FACEBOOK_ACCESS_TOKEN'),
            'page_id': os.getenv('FACEBOOK_PAGE_ID')
        },
        'instagram': {
            'access_token': os.getenv('INSTAGRAM_ACCESS_TOKEN')
        },
        'tiktok': {
            'access_token': os.getenv('TIKTOK_ACCESS_TOKEN')
        },
        'twitter': {
            'bearer_token': os.getenv('TWITTER_BEARER_TOKEN')
        }
    }
    
    # Course Settings
    COURSE_CREATION_INTERVAL_DAYS = 60  # Every 2 months
    DEFAULT_COURSES = [
        {'name': 'Facebook Blueprint', 'price': 500, 'currency': 'ZAR'},
        {'name': 'Academy Six', 'price': 1800, 'currency': 'ZAR'},
        {'name': 'Little Learners', 'price': 250, 'currency': 'ZAR'}
    ]
    
    # Business Information
    BUSINESS_INFO = {
        'name': 'LearnHub',
        'address': 'Cape Town, South Africa',
        'phone': '076 424 5061',
        'whatsapp': '2764245061',
        'email': 'support@learnhub.com'
    }
    
    # Compliance Settings
    COMPLIANCE = {
        'south_africa': True,
        'namibia': True,
        'botswana': True,
        'gdpr': True,
        'popia': True
    }
    
    # AI Settings
    AI_AGENTS = {
        'marketing': {'enabled': True, 'frequency': 'daily'},
        'customer_support': {'enabled': True, 'model': 'Megan'},
        'payment': {'enabled': True, 'auto_payout': True},
        'security': {'enabled': True, 'monitoring': True}
    }

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
