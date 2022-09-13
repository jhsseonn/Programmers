class EvenOrOdd {
    public String evenOrOdd(int num) {
        return num % 2 == 0 ? "Even" : "Odd";
    }

    public static void main(String[] args) {
        EvenOrOdd evenOrOdd = new EvenOrOdd();
        System.out.println("결과: "+evenOrOdd.evenOrOdd(3));
        System.out.println("결과: "+evenOrOdd.evenOrOdd(4));
    }
}
