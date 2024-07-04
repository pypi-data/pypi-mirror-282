import altair as alt
import json

class AltairGraphComparer:
    @staticmethod
    def get_chart_json(chart):
        if isinstance(chart, str):
            return json.loads(chart)
        else:
            return json.loads(chart.to_json())

    @staticmethod
    def compare_charts(chart1, chart2):
        json1 = AltairGraphComparer.get_chart_json(chart1)
        json2 = AltairGraphComparer.get_chart_json(chart2)

        datasets1 = json1.get('datasets', {})
        datasets2 = json2.get('datasets', {})

        dataset_values1 = next(iter(datasets1.values()), [])  # Get first dataset values
        dataset_values2 = next(iter(datasets2.values()), [])  # Get first dataset values

        differences = {}

        def compare_dataset_values(json1, json2):
            # Load JSON strings into dictionaries
            dict1 = json.loads(json1)
            dict2 = json.loads(json2)

            # Get datasets values ignoring keys
            datasets1 = next(iter(dict1.get('datasets', {}).values()), [])
            datasets2 = next(iter(dict2.get('datasets', {}).values()), [])

            # Compare dataset values
            if datasets1 == datasets2:
                return True
            else:
                return False

        AltairGraphComparer.match(dataset_values1, dataset_values2)
        return differences
    
    @staticmethod
    def match(chart1, chart2):
        json1 = AltairGraphComparer.get_chart_json(chart1)
        json2 = AltairGraphComparer.get_chart_json(chart2)

        # Compare chart type ("mark" attribute)
        mark1 = json1.get('mark')
        mark2 = json2.get('mark')
        if mark1 != mark2:
            print(f"Chart type is different: {mark1} != {mark2}")
            return False

        # Get datasets values ignoring keys
        datasets1 = next(iter(json1.get('datasets', {}).values()), [])
        datasets2 = next(iter(json2.get('datasets', {}).values()), [])

        # Compare dataset values
        if datasets1 == datasets2:
            return True
        else:
            differences = []
            for idx, (item1, item2) in enumerate(zip(datasets1, datasets2)):
                for key in item1.keys() | item2.keys():
                    val1 = item1.get(key)
                    val2 = item2.get(key)
                    if val1 != val2:
                        differences.append(f"Dataset[{idx}].{key}: {val1} != {val2}")
            
            if differences:
                print("Differences in dataset values:")
                for diff in differences:
                    print(diff)
            return False


# Example usage
if __name__ == "__main__":
    import json

    # JSON input of the new chart to compare
    chart1 = """
    {
        "config": {
            "view": {"continuousWidth": 400, "continuousHeight": 300}
        },
        "data": {"name": "data-679d61f96919a9b00678a3858e27aa15"},
        "mark": "bar",
        "encoding": {
            "tooltip": [{"field": "month", "type": "nominal"}, {"field": "booking_duration", "type": "quantitative"}],
            "x": {"axis": {"labelAngle": -45, "title": "Month"}, "field": "month", "sort": null, "type": "nominal"},
            "y": {"field": "booking_duration", "title": "Average Booking Duration (Days)", "type": "quantitative"}
        },
        "selection": {"selector001": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}},
        "title": "Average Booking Duration by Month",
        "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json",
        "datasets": {"data-679d61f96919a9b00678a3858e27aa15": [{"month": "January", "booking_duration": -778.581308411215, "month_order": 0}]}
    }
    """

    # Example usage: Compare with an existing chart JSON (replace with actual JSON)
    chart2 = """
    {
        "config": {
            "view": {"continuousWidth": 400, "continuousHeight": 300}
        },
        "data": {"name": "data-2"},
        "mark": "bar",
        "encoding": {
            "tooltip": [{"field": "month", "type": "nominal"}, {"field": "booking_duration", "type": "quantitative"}],
            "x": {"axis": {"title": "Month"}, "field": "month", "sort": null, "type": "nominal"},
            "y": {"field": "booking_duration", "title": "Average Booking Duration", "type": "quantitative"}
        },
        "selection": {"selector001": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}},
        "title": "Average Monthly Booking Duration",
        "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json",
        "datasets": {"data-2": [{"month": "January", "booking_duration": -778.581308411215, "month_order": 0}]}
    }
    """


    # Compare the charts
    comparer = AltairGraphComparer()

    is_same_graph = comparer.match(chart1, chart2)

    print("Are the charts the same? ", is_same_graph)
