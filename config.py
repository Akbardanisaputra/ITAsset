"""
Application Configuration
=========================
Central configuration for the IT Asset Lifecycle Management System.
Switch SQLALCHEMY_DATABASE_URI to PostgreSQL when ready to migrate.
"""

import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration class."""

    # --- Security ---
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')

    # --- Database ---
    # SQLite for development; swap to PostgreSQL URI for production:
    # 'postgresql://user:pass@host:port/dbname'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f'sqlite:///{os.path.join(BASE_DIR, "instance", "app.db")}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Flask-WTF ---
    WTF_CSRF_ENABLED = True

    # --- Application ---
    ITEMS_PER_PAGE = 20
    SERVICE_OVERDUE_DAYS = 7  # Days before a vendor service is flagged overdue
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
