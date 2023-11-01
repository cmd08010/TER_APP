"""API for Prices model"""
from prices.models import Prices
import logging
from datetime import datetime
import pytz

logger = logging.getLogger('ter')

class PricesAPI:
    """API for Prices model"""

    # TBD: exception handling, testing
    def get_days_last_created_price_schedule(day):
        """Traverse Prices to find item with lastest creation date for given day"""
        logger.info(f"PricesAPI.get_days_last_created_price_schedule(day={day})")
        created = datetime(2000,1, 1, 0, 0, 0, 0, pytz.UTC)
        s = latest = None
        for p in Prices.objects.all():
            s = p.schedule
            date = s["date"]
            logger.debug(f"PricesAPI.get_days_last_created_price_schedule() schedule={s} created={p.created} date={date} created-base={created}")
            if (date == day.isoformat() and p.created > created):
                logger.debug(f"PricesAPI.get_days_last_created_price_schedule() p.created {p.created} latest={s}")
                created = p.created
                latest = s
            else:
                logger.debug(f"PricesAPI.get_days_last_created_price_schedule() Dates NOT equal! schedule.date={date} day={day}")

        return (latest)