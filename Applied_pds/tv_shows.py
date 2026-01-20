import pandas as pd


def tackle_tv_shows(json_path: str) -> None:
    tv_shows_json = pd.read_json(json_path)
    tv_shows = pd.json_normalize(
        data=tv_shows_json["shows"],
        record_path="episodes",
        meta=["show", "runtime", "network"],
    )

    tv_shows_names = ("The X-Files", "Lost", "Buffy the Vampire Slayer")
    with pd.ExcelWriter("episodes.xlsx") as episodes_obj:
        for tv_name in tv_shows_names:
            tv_df = tv_shows[tv_shows["show"] == tv_name]
            tv_df.to_excel(
                excel_writer=episodes_obj,
                sheet_name=tv_name,
                index=False
            )


if __name__ == '__main__':
    tackle_tv_shows("cha12/tv_shows.json")