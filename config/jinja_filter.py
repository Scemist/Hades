def apply_jinja_filters(app):
    def get_category_color(category=None):
        match category:
            case "danger":
                return "bg-red-800"
            case _:
                return "bg-blue-800"

    app.jinja_env.filters["category_color"] = get_category_color