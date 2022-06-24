from google.cloud import bigquery

DATASET = "IP_CoffeeHR"



def load(table: str, schema: list[dict]):
    def _load(rows: list[dict]) -> int:
        client = bigquery.Client()
        output_rows = (
            client.load_table_from_json(
                rows,
                f"{DATASET}.{table}",
                job_config=bigquery.LoadJobConfig(
                    schema=schema,
                    create_disposition="CREATE_IF_NEEDED",
                    write_disposition="WRITE_TRUNCATE",
                ),
            )
            .result()
            .output_rows
        )

        return output_rows

    return _load
