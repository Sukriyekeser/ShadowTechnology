import sentry_sdk

sentry_sdk.init(
    dsn="https://6064789331b96b62a0b48b86d7969d38@o4507080777269248.ingest.de.sentry.io/4507080794964048",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

