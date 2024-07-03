from opengate_data.utils.utils import validate_type


class SelectBuilder:
    """ Select Builder """

    VALID_FIELDS = {
        "value", "date", "at", "from", "tags", "feedId",
        "scoring.performance", "scoring.qrating", "provType"
    }

    def __init__(self):
        self._select_template = {"select": []}

    def add(self, name: str, fields: list[[str, tuple[str, str]]]):
        """
        Adds name and fields in select.

        Args:
            name (str): The name of the data stream.
            fields (list): A list of fields to retrieve, each field being a string or a tuple with 'field' and optional 'alias'.

        Returns:
            SelectBuilder: Returns itself to allow for method chaining.

        Example:
            builder.add("provision.device.identifier", [
                ("value", "id"),
                ("date", "date_alias")
            ]).add("provision.device.location", ["value.postal"])
        """
        validate_type(name, str, "name")
        validate_type(fields, list, "fields")

        processed_fields = []
        for field in fields:
            if isinstance(field, str):
                if field.split('.')[0] not in self.VALID_FIELDS:
                    raise ValueError(f"Invalid field: {field}")
                processed_fields.append({"field": field})
            elif isinstance(field, tuple):
                validate_type(field[0], str, "field[0]")
                if field[0].split('.')[0] not in self.VALID_FIELDS:
                    raise ValueError(f"Invalid field: {field[0]}")
                validate_type(field[1], str, "field[1]")
                processed_fields.append({"field": field[0], "alias": field[1]})
            else:
                raise ValueError("Each field must be either a string or a tuple with 'field' and optional 'alias'")

        select_entry = {"name": name, "fields": processed_fields}
        elements = self._select_template["select"]
        if not elements:
            self._select_template["select"].append(select_entry)
        else:
            exists_element = False
            for element in elements:
                if element["name"] == name:
                    exists_element = True
                    for input_field in processed_fields:
                        field_exists = False
                        for existing_field in element["fields"]:
                            if existing_field["field"] == input_field["field"]:
                                field_exists = True
                                if "alias" in input_field:
                                    existing_field["alias"] = input_field["alias"]
                        if not field_exists:
                            element["fields"].append(input_field)
            if not exists_element:
                self._select_template["select"].append(select_entry)
        return self

    def build(self):
        """
        Builds the final select clause.

        Returns:
            list: The final select clause.

        Raises:
            ValueError: If no select criteria have been added.
        """
        if not self._select_template["select"]:
            raise ValueError("No select criteria have been added")
        return self._select_template["select"]
