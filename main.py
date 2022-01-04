from app.parser import Parser
import os

if __name__ == "__main__":
    parser = Parser()

    exampleFile = os.path.join(
        os.path.dirname(__file__), 'uploads', 'mock.json'
    )

    parser = Parser()
    parser.openFile(exampleFile)

    examples = parser.getExamples()

    print("Mocking {count} examples:".format(count=len(examples)))

    for idx, example in enumerate(examples):
        print("Example {index}: ".format(index=(idx+1)), example['name'])

    print('\n {lb}'.format(lb=('=' * 100)))
    for idx, example in enumerate(examples):
        if not example['request'].getUri():
            continue

        # Mock Name
        print("Mock #{index}: ".format(index=(idx + 1)), example['name'])

        # Method [GET, POST]
        print(
            "\t URI:",
            '[{req_method}]'.format(
                req_method=example['request'].getMethod()
            ),
            example['request'].getUri()
        )

        # Content Type
        print(
            '\t Content-Type: {header}'.format(
                header=example['request'].getHeader('Content-Type')
            )
        )

        # Request params (in Body)
        print(
            '\t Body: {body}'.format(
                body=', '.join(
                    [
                        '='.join([body['key'], body['value']])
                        for body in example['request'].getBody()
                    ]
                )
            )
        )

        # Response Type
        print(
            '\t Response Type: {header}'.format(
                header=example['response'].getHeader('Content-Type')
            )
        )

        # Response Data
        print(
            '\t Response Body: {body}'.format(
                body=example['response'].getBody()
            )
        )

    print('\n\n')
    parser.run()
