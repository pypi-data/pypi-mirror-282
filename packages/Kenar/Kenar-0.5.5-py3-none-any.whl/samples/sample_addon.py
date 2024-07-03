from kenar import (
    CreatePostAddonRequest,
    GetUserAddonsRequest,
    DeleteUserAddonRequest,
    GetPostAddonsRequest,
    DeletePostAddonRequest,
    CreateUserAddonRequest,
    IconName,
    Icon,
    TitleRow,
    SubtitleRow,
    SelectorRow,
    ScoreRow,
    LegendTitleRow,
    GroupInfo,
    EventRow,
    EvaluationRow,
    DescriptionRow,
    Color,
    WideButtonBar,
)

from samples.sample_app import app

if __name__ == "__main__":
    rsp = app.addon.upload_image("/Users/nastaran/Downloads/s.jpg")
    print(rsp.image_name)
    image_name = rsp.image_name

    # create widgets for addon
    title_row = TitleRow(
        text="این یک نمونه تایتل میباشد", text_color=Color.TEXT_SECONDARY
    )

    subtitle_row = SubtitleRow(text="این یک سابتایتل میباشد")

    desc_row = DescriptionRow(
        text="سلام - این یک ویجت تستی میباشد.",
        has_divider=True,
        is_primary=True,
        expandable=False,
        padded=True,
    )

    eval_row = EvaluationRow(
        indicator_text="متن اندیکاتور",
        indicator_percentage=50,
        indicator_icon=Icon(icon_name=IconName.DOWNLOAD),
        indicator_color=Color.SUCCESS_PRIMARY,
        left=EvaluationRow.Section(
            text="سمت چپ",
            text_color=Color.TEXT_SECONDARY,
            section_color=Color.SUCCESS_PRIMARY,
        ),
        middle=EvaluationRow.Section(
            text="وسط",
            text_color=Color.TEXT_SECONDARY,
            section_color=Color.TEXT_PRIMARY,
        ),
        right=EvaluationRow.Section(
            text="سمت راستی",
            text_color=Color.TEXT_SECONDARY,
            section_color=Color.TEXT_SECONDARY,
        ),
    )

    event_row = EventRow(
        title="تایتل",
        subtitle="سابتایتل",
        has_indicator=False,
        image_url=image_name,
        label="لیبل",
        has_divider=True,
        link="https://www.test.com",
        padded=True,
        icon=Icon(icon_name=IconName.ADD),
    )

    group_info = GroupInfo(
        has_divider=True,
        items=[
            GroupInfo.GroupInfoItem(title="تایتل ۱", value="مقدار ۱"),
            GroupInfo.GroupInfoItem(title="تایتل ۲", value="مقدار ۲"),
            GroupInfo.GroupInfoItem(title="تایتل ۳", value="مقدار ۳"),
        ],
    )

    legend_title_row = LegendTitleRow(
        title="ارائه خدمت با کنار دیوار",
        subtitle="",
        has_divider=True,
        image_url="logo",
        tags=[
            LegendTitleRow.Tag(
                text="احراز",
                icon=Icon(icon_name=IconName.VERIFIED),
                bg_color=LegendTitleRow.Tag.BackgroundColor.GRAY,
            ),
            LegendTitleRow.Tag(
                text="کارشناسی",
                icon=Icon(icon_name=IconName.CAR_INSPECTED),
                bg_color=LegendTitleRow.Tag.BackgroundColor.TRANSPARENT,
            ),
            LegendTitleRow.Tag(
                text="پرداخت امن",
                icon=Icon(icon_name=IconName.ADD),
                bg_color=LegendTitleRow.Tag.BackgroundColor.RED,
            ),
        ],
    )

    score_row_1 = ScoreRow(
        title="مدل امتیاز کیفی",
        descriptive_score="بسیار عالی",
        score_color=Color.TEXT_SECONDARY,
        link="",
        has_divider=True,
        icon=Icon(icon_name=IconName.ADD),
    )

    score_row_2 = ScoreRow(
        title="مدل امتیاز درصدی",
        percentage_score=100,
        score_color=Color.TEXT_SECONDARY,
        link="",
        has_divider=True,
        icon=Icon(icon_name=IconName.ADD),
    )

    selector_row = SelectorRow(
        title="این یک ویجت سلکتور میباشد",
        has_divider=True,
        has_arrow=True,
        icon=Icon(icon_name=IconName.INFO),
        link="https://www.test.com",
    )

    wide_button_bar = WideButtonBar(
        button=WideButtonBar.Button(
            title="به سمت سایت شما", link="https://www.test.com"
        ),
    )

    resp = app.addon.create_post_addon(
        access_token="ory_at_PB9eAI5jIEZU6J7ic1mNDoxaNsvgfZHIujMAWAm1LMk.sPxBtAsxGMV-mJiKron_FZpjyvrhlNoUJM-J3_Ne840",
        data=CreatePostAddonRequest(
            token="gZW5uQcs",
            widgets=[
                title_row,
                subtitle_row,
                desc_row,
                eval_row,
                event_row,
                group_info,
                selector_row,
                wide_button_bar,
            ],
        ),
    )
    print(resp)

    resp = app.addon.get_post_addons(data=GetPostAddonsRequest(token="gZW5uQcs"))
    print(resp)

    resp = app.addon.delete_post_addon(
        data=DeletePostAddonRequest(token="gZW5uQcs")
    )
    print(resp)

    resp = app.addon.get_post_addons(data=GetPostAddonsRequest(token="gZW5uQcs"))
    print(resp)

    resp = app.addon.create_user_addon(
        access_token="ory_at_PB9eAI5jIEZU6J7ic1mNDoxaNsvgfZHIujMAWAm1LMk.sPxBtAsxGMV-mJiKron_FZpjyvrhlNoUJM-J3_Ne840",
        data=CreateUserAddonRequest(
            phone="09035718581",
            widgets=[desc_row],
            notes="test note",
            categories=[],
        ),
    )
    print(resp)
    user_addon_id = resp.id

    resp = app.addon.get_user_addons(data=GetUserAddonsRequest(phone="09035718581"))
    print(resp)

    resp = app.addon.delete_user_addon(data=DeleteUserAddonRequest(id=user_addon_id))
    print(resp)

    resp = app.addon.get_user_addons(data=GetUserAddonsRequest(phone="09035718581"))
    print(resp)
