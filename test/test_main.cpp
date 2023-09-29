#include <gtest/gtest.h>

TEST(SampleSuite, SampleTest) {
    EXPECT_STRNE("Hello", "World");
    EXPECT_EQ(25, 5*5);
}
