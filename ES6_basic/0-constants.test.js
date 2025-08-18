import { taskFirst, taskNext } from "./0-constants";

test('taskFirst return const str', () => {
    expect(taskFirst()).toBe('I prefer const when I can.');
});

test('taskNext return concatened let string', () => {
    expect(taskNext()).toBe('But sometimes let is okay')
})