# tableformat.py

def print_table(records, fields, formatter):
    formatter.start()
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname, 'undef') for fieldname in fields]
        formatter.row(rowdata)
    formatter.end()

class TableFormatter(object):
    def start(self):
        pass

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError

    def end(self):
        pass

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print("%10s" % h, end=' ')
        print()
        print(("-"*10 + " ")*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print("%10s" % d, end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def start(self):
        print('<table>')

    def headings(self, headers):
        print("<tr>", end=' ')
        for h in headers:
            print("<th>%s</th>" % h, end=' ')
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end=' ')
        for d in rowdata:
            print("<td>%s</td>" % d, end=' ')
        print("</tr>")

    def end(self):
        print('</table>')

# Sample
if __name__ == '__main__':
    import stock
    portfolio = stock.read_portfolio("../../Data/portfolio.dat")
    formatter = HTMLTableFormatter()
    print_table(portfolio,['name','shares','price'], formatter)




