from .tabledetector import TableDetector

def detect(pdfPath, type="consolidated", rotation=False, method='detect'):
    detector = TableDetector(pdfPath, type, rotation, method)
    return detector.main()