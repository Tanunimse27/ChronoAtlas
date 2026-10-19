def to_internal_year(year, era):
    """Convert a historical BCE/CE year to an internal number."""

    if year < 1:
        raise ValueError("Historical year must be at least 1.")

    if era == "BCE":
        return 1 - year

    elif era == "CE":
        return year

    else:
        raise ValueError("Era must be 'BCE' or 'CE'.")


def get_time_window(selected_year, default_years=20):
    starting_year=selected_year - default_years
    end_year= selected_year + default_years

    return starting_year, end_year