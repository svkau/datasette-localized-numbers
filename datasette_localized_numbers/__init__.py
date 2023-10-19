from datasette import hookimpl
from babel import Locale
from babel.core import UnknownLocaleError
from babel.numbers import format_decimal, format_currency


def show_number(value):
    try:
        number = float(value)
        return format_decimal(number, locale="sv_SE")
    except (ValueError, TypeError):
        return value


def show_currency(value):
    try:
        number = float(value)
        return format_currency(number, currency="SEK", locale="sv_SE")
    except (ValueError, TypeError):
        return value


@hookimpl
def render_cell(value, column, table, database, datasette):

    plugin_config = datasette.plugin_config(
        "datasette-localized-numbers", database=database, table=table
    )
    if plugin_config:

        if 'locale' in plugin_config:
            locale_id = plugin_config['locale']
            locale_data = [locale_id[:2], locale_id[3:]]

            try:
                cur_locale = Locale(language=locale_data[0], territory=locale_data[1])

            except UnknownLocaleError:
                return None

            else:

                if isinstance(value, str):
                    try:
                        value = float(value)
                    except (ValueError, TypeError):
                        pass

                if isinstance(value, (int, float)):
                    if 'format_number' in plugin_config and column in plugin_config['format_number']:
                        return format_decimal(value, locale=cur_locale)

                    elif 'format_currency' in plugin_config and column in [col[0] for col in
                                                                           plugin_config['format_currency']]:
                        currency_symbol = ''
                        for col in plugin_config['format_currency']:
                            if col[0] == column:
                                currency_symbol = col[1]

                        return format_currency(value, currency=currency_symbol, locale=cur_locale)

                else:
                    return None
        else:
            return None
    else:
        return None


@hookimpl
def prepare_jinja2_environment(env):
    env.filters["number"] = lambda u: show_number(u)
    env.filters["currency"] = lambda u: show_currency(u)
