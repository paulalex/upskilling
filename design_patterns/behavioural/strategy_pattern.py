from __future__ import annotations
from abc import ABC, abstractmethod

class ExportStrategy:
    @abstractmethod
    def export(self, data):
        pass

class CsvExport(ExportStrategy):
    def export(self, data):
        print(f"Exporting {data} in CSV format")

class ParqueExport(ExportStrategy):
    def export(self, data):
        print(f"Exporting {data} in Parque format")

class JsonExport(ExportStrategy):
    def export(self, data):
        print(f"Exporting {data} in JSON format")

class XMLExport(ExportStrategy):
    def export(self, data):
        print(f"Exporting {data} in XML")

class ExportContext:
    _strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy

    def export_data(self, data):
        self._strategy.export(data)

if __name__ =="__main__":
    export_context = ExportContext()
    export_strategies = [CsvExport(), ParqueExport(), JsonExport(), XMLExport()]
    data = "some data that needs to be exported"

    for export_strategy in export_strategies:
        export_context.set_strategy(export_strategy)
        export_context.export_data(data)
