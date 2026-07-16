import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "diana"]
    actions = [
        "run", "eat", "sleep", "grab",
        "move", "climb", "swim", "release"
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)

        yield (player, action)


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events[index]

        del events[index]

        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_generator = gen_event()
    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events = events + [next(event_generator)]

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
